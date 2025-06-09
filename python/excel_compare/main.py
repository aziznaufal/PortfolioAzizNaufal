import pandas as pd
import os
from datetime import datetime
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext, ttk

def col_idx_to_excel_col(idx):
    result = ''
    while idx >= 0:
        result = chr(idx % 26 + ord('A')) + result
        idx = idx // 26 - 1
    return result

def compare_files(file1, file2, output_dir, text_widget, progress_bar, root):
    try:
        sheets1 = pd.read_excel(file1, sheet_name=None)
        sheets2 = pd.read_excel(file2, sheet_name=None)
    except Exception as e:
        messagebox.showerror("Error", f"Gagal baca file Excel:\n{e}")
        return

    sheets1_names = set(sheets1.keys())
    sheets2_names = set(sheets2.keys())

    text_widget.insert(tk.END, f"📄 Sheets only in File 1: {sheets1_names - sheets2_names}\n")
    text_widget.insert(tk.END, f"📄 Sheets only in File 2: {sheets2_names - sheets1_names}\n\n")

    common_sheets = sheets1_names & sheets2_names
    if not common_sheets:
        text_widget.insert(tk.END, "⚠️ Tidak ada sheet yang sama di kedua file.\n")
        return

    progress_bar['maximum'] = len(common_sheets)
    progress_bar['value'] = 0
    root.update_idletasks()

    for i, sheet in enumerate(common_sheets, start=1):
        text_widget.insert(tk.END, f"🔍 Comparing sheet: {sheet}\n")
        df1 = sheets1[sheet]
        df2 = sheets2[sheet]

        try:
            common_columns = sorted(list(set(df1.columns) & set(df2.columns)))
            if not common_columns:
                text_widget.insert(tk.END, f"⚠️ No common columns to compare in sheet '{sheet}'\n")
                continue

            df1 = df1[common_columns].reset_index(drop=True)
            df2 = df2[common_columns].reset_index(drop=True)

            min_len = min(len(df1), len(df2))
            df1 = df1.iloc[:min_len]
            df2 = df2.iloc[:min_len]

            if df1.equals(df2):
                text_widget.insert(tk.END, "✅ Sheets are identical.\n\n")
            else:
                text_widget.insert(tk.END, "❌ Sheets differ.\n")
                differences = []
                count = 1

                for row_idx in range(min_len):
                    for col_idx, col_name in enumerate(common_columns):
                        val1 = df1.at[row_idx, col_name]
                        val2 = df2.at[row_idx, col_name]

                        if pd.isna(val1) and pd.isna(val2):
                            continue
                        elif (val1 != val2) and not (pd.isna(val1) and not pd.isna(val2)) and not (not pd.isna(val1) and pd.isna(val2)):
                            cell = f"{col_idx_to_excel_col(col_idx)}{row_idx+1}"
                            differences.append(f"{count}. cell {cell}: in file1 -> \"{val1}\" but in file2 -> \"{val2}\"")
                            count += 1

                if differences:
                    text_widget.insert(tk.END, f"Total differences found: {len(differences)}\n")
                    # for diff in differences:
                    #     text_widget.insert(tk.END, diff + "\n")

                    date = datetime.now().strftime("%Y%m%d_%H%M%S")
                    safe_sheet_name = "".join(c if c.isalnum() else "_" for c in sheet)
                    txt_output_path = os.path.join(output_dir, f'diff_list_{safe_sheet_name}_{date}.txt')

                    with open(txt_output_path, 'w', encoding='utf-8') as f:
                        f.write(f"Differences in sheet: {sheet}\n\n")
                        f.write("\n".join(differences))

                    text_widget.insert(tk.END, f"📁 Differences saved to text file: {txt_output_path}\n\n")
                else:
                    text_widget.insert(tk.END, "⚠️ No visible differences detected after detailed check.\n\n")

        except Exception as e:
            text_widget.insert(tk.END, f"⚠️ Error comparing sheet '{sheet}': {e}\n\n")

        progress_bar['value'] = i
        root.update_idletasks()

    messagebox.showinfo("Selesai", "Compare done!")

def browse_file(entry):
    filename = filedialog.askopenfilename(filetypes=[("Excel files", "*.xls *.xlsx")])
    if filename:
        entry.delete(0, tk.END)
        entry.insert(0, filename)

def browse_folder(entry):
    folder = filedialog.askdirectory()
    if folder:
        entry.delete(0, tk.END)
        entry.insert(0, folder)

def start_compare(file1_entry, file2_entry, output_entry, text_widget, progress_bar, root):
    file1 = file1_entry.get()
    file2 = file2_entry.get()
    output_dir = output_entry.get()

    if not os.path.isfile(file1):
        messagebox.showerror("Error", "File 1 tidak valid.")
        return
    if not os.path.isfile(file2):
        messagebox.showerror("Error", "File 2 tidak valid.")
        return
    if not os.path.isdir(output_dir):
        messagebox.showerror("Error", "Folder output tidak valid.")
        return

    text_widget.delete(1.0, tk.END)
    compare_files(file1, file2, output_dir, text_widget, progress_bar, root)

def main():
    root = tk.Tk()
    root.title("Excel Compare Tool")
    root.geometry("800x600")
    root.resizable(False, False)  # Disable resize

    # File 1
    tk.Label(root, text="File Excel 1:").grid(row=0, column=0, sticky='w', padx=5, pady=5)
    file1_entry = tk.Entry(root, width=70)
    file1_entry.grid(row=0, column=1, padx=5, pady=5)
    tk.Button(root, text="Browse", command=lambda: browse_file(file1_entry)).grid(row=0, column=2, padx=5, pady=5)

    # File 2
    tk.Label(root, text="File Excel 2:").grid(row=1, column=0, sticky='w', padx=5, pady=5)
    file2_entry = tk.Entry(root, width=70)
    file2_entry.grid(row=1, column=1, padx=5, pady=5)
    tk.Button(root, text="Browse", command=lambda: browse_file(file2_entry)).grid(row=1, column=2, padx=5, pady=5)

    # Output folder
    tk.Label(root, text="Folder Output:").grid(row=2, column=0, sticky='w', padx=5, pady=5)
    output_entry = tk.Entry(root, width=70)
    output_entry.grid(row=2, column=1, padx=5, pady=5)
    tk.Button(root, text="Browse", command=lambda: browse_folder(output_entry)).grid(row=2, column=2, padx=5, pady=5)

    # Progress bar
    progress_bar = ttk.Progressbar(root, orient=tk.HORIZONTAL, length=600, mode='determinate')
    progress_bar.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

    # Compare button
    tk.Button(root, text="Compare Now", command=lambda: start_compare(file1_entry, file2_entry, output_entry, text_area, progress_bar, root)).grid(row=4, column=1, pady=10)

    # Text area for output
    text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=90, height=25)
    text_area.grid(row=5, column=0, columnspan=3, padx=10, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()

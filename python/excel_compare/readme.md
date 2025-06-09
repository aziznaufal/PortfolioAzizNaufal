# 📈 Excel Compare App

A simple and powerful Windows GUI app to **compare two Excel files** and detect cell-level differences — built with Python, Pandas, and Tkinter.

---

## 🚀 Features

* 🔍 **Compare all sheets** between two Excel files
* 📌 Detects and lists **cell-by-cell differences**
* 🛍 Shows difference like:
  `1. cell A20: in file1 -> "ABC" but in file2 -> "DEF"`
* 📂 **File browser support**: Easily select source files
* 📁 **Custom output location**: Save results anywhere you choose
* 📄 Output saved in `.txt` format, readable and simple
* 🔐 Read-only operation – no data is modified
* 🎯 Fixed-size window, with progress bar and completion notification

---

## 🛠 Built With

* [Python 3](https://www.python.org/)
* [Tkinter](https://wiki.python.org/moin/TkInter) – for GUI
* [Pandas](https://pandas.pydata.org/) – for data comparison
* [openpyxl / xlrd](https://openpyxl.readthedocs.io/) – for Excel file reading
* [PyInstaller](https://pyinstaller.org/) – for EXE bundling

---

## 📅 How to Use

1. Open the app (`Excel Compare.exe`)
2. Click **Browse** to select the two Excel files to compare
3. Choose where to save the output `.txt` result
4. Click **Compare**
5. Wait for the progress bar to complete
6. A notification will show when the comparison is done

---

## 📆 Installation

To build the app from source:

1. Clone the repo:

   ```bash
   git clone 
   cd excel-compare-app
   ```

2. Install dependencies:

   ```bash
   pip install pandas openpyxl xlrd
   ```

3. Run the app:

   ```bash
   python excel_compare_app.py
   ```

To generate the Windows `.exe` file:

```bash
pyinstaller --onefile --windowed --name "Excel Compare" excel_compare_app.py
```

---

## 🧪 Example Output

```
1. cell A20: in file1 -> "ABC" but in file2 -> "DEF"
2. cell C25: in file1 -> "1000" but in file2 -> "1200"
...
```

---

## 📁 Output Sample

* File type: `.txt`
* Automatically numbered difference list
* Shows sheet name and cell reference

---

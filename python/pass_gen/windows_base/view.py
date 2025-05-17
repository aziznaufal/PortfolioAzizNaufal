import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class PasswordView:
    def __init__(self, root):
        self.root = root
        self.root.title("Modern Password Generator")
        self.root.geometry("420x350")
        self.root.resizable(False, False)
        self.root.configure(bg="#2c3e50")

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TLabel", background="#2c3e50", foreground="white", font=("Segoe UI", 10))
        style.configure("TCheckbutton", background="#2c3e50", foreground="white", font=("Segoe UI", 10))
        style.configure("TButton", font=("Segoe UI", 10, "bold"), padding=6)
        style.configure("TEntry", font=("Segoe UI", 10))

        self.length_var = tk.StringVar(value="12")
        self.password_var = tk.StringVar()
        self.use_upper = tk.BooleanVar(value=True)
        self.use_lower = tk.BooleanVar(value=True)
        self.use_digits = tk.BooleanVar(value=True)
        self.use_symbols = tk.BooleanVar(value=False)

        self.create_widgets()

    def create_widgets(self):
        frame = ttk.Frame(self.root, padding=20)
        frame.pack(expand=True)

        ttk.Label(frame, text="Password Length:").grid(row=0, column=0, sticky="w")
        ttk.Entry(frame, textvariable=self.length_var, width=10).grid(row=0, column=1, sticky="w")

        ttk.Checkbutton(frame, text="Include Uppercase", variable=self.use_upper).grid(row=1, column=0, columnspan=2, sticky="w")
        ttk.Checkbutton(frame, text="Include Lowercase", variable=self.use_lower).grid(row=2, column=0, columnspan=2, sticky="w")
        ttk.Checkbutton(frame, text="Include Digits", variable=self.use_digits).grid(row=3, column=0, columnspan=2, sticky="w")
        ttk.Checkbutton(frame, text="Include Symbols", variable=self.use_symbols).grid(row=4, column=0, columnspan=2, sticky="w")

        ttk.Button(frame, text="Generate Password", command=self.on_generate_clicked).grid(row=5, column=0, columnspan=2, pady=(15, 5), sticky="ew")
        ttk.Entry(frame, textvariable=self.password_var, width=40, state='readonly', justify='center').grid(row=6, column=0, columnspan=2, pady=(10, 5))
        ttk.Button(frame, text="Copy to Clipboard", command=self.on_copy_clicked).grid(row=7, column=0, columnspan=2, pady=(0, 5), sticky="ew")

    def on_generate_clicked(self):
        if self.controller:
            self.controller.handle_generate()

    def on_copy_clicked(self):
        if self.controller:
            self.controller.handle_copy()

    def show_password(self, password):
        self.password_var.set(password)

    def show_error(self, title, message):
        messagebox.showerror(title, message)

    def show_warning(self, title, message):
        messagebox.showwarning(title, message)

    def show_info(self, title, message):
        messagebox.showinfo(title, message)

    def set_controller(self, controller):
        self.controller = controller
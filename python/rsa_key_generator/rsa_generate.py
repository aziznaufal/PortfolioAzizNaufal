import tkinter as tk
from tkinter import filedialog, messagebox
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
import os

def generate_key():
    passphrase = passphrase_entry.get().encode()
    key_size = int(bit_entry.get())
    private_path = private_output_entry.get()
    public_path = public_output_entry.get()

    if not passphrase or not private_path or not key_size:
        messagebox.showerror("Error", "Field tidak boleh kosong.")
        return

    try:
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=key_size,
            backend=default_backend()
        )

        # Simpan private key terenkripsi
        encrypted_pem = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.BestAvailableEncryption(passphrase)
        )

        with open(private_path, 'wb') as f:
            f.write(encrypted_pem)

        # Simpan public key
        public_key = private_key.public_key()
        public_pem = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )

        # Public key path
        if not public_path:
            public_path = private_path.replace(".pem", "_public.pem")

        with open(public_path, 'wb') as f:
            f.write(public_pem)

        messagebox.showinfo("Sukses", f"Private Key disimpan di:\n{private_path}\n\nPublic Key disimpan di:\n{public_path}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def browse_private_file():
    filepath = filedialog.asksaveasfilename(
        defaultextension=".pem",
        filetypes=[("PEM Files", "*.pem"), ("All Files", "*.*")]
    )
    if filepath:
        private_output_entry.delete(0, tk.END)
        private_output_entry.insert(0, filepath)

def browse_public_file():
    filepath = filedialog.asksaveasfilename(
        defaultextension=".pem",
        filetypes=[("PEM Files", "*.pem"), ("All Files", "*.*")]
    )
    if filepath:
        public_output_entry.delete(0, tk.END)
        public_output_entry.insert(0, filepath)

# UI setup
root = tk.Tk()
root.title("RSA Encrypted Key Generator + Public Key")

tk.Label(root, text="Passphrase:").grid(row=0, column=0, sticky="e")
passphrase_entry = tk.Entry(root, width=40, show="*")
passphrase_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Key Size (bit):").grid(row=1, column=0, sticky="e")
bit_entry = tk.Entry(root, width=40)
bit_entry.insert(0, "2048")
bit_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Private Key Output:").grid(row=2, column=0, sticky="e")
private_output_entry = tk.Entry(root, width=40)
private_output_entry.grid(row=2, column=1, padx=5, pady=5)
tk.Button(root, text="Browse", command=browse_private_file).grid(row=2, column=2, padx=5, pady=5)

tk.Label(root, text="Public Key Output (opsional):").grid(row=3, column=0, sticky="e")
public_output_entry = tk.Entry(root, width=40)
public_output_entry.grid(row=3, column=1, padx=5, pady=5)
tk.Button(root, text="Browse", command=browse_public_file).grid(row=3, column=2, padx=5, pady=5)

tk.Button(root, text="Generate Keys", command=generate_key, bg="#4CAF50", fg="white").grid(row=4, column=1, pady=10)

root.mainloop()

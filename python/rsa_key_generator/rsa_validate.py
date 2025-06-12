import tkinter as tk
from tkinter import filedialog, messagebox
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend

def load_private_key(path, password):
    with open(path, "rb") as key_file:
        return serialization.load_pem_private_key(
            key_file.read(),
            password=password.encode() if password else None,
            backend=default_backend()
        )

def load_public_key(path):
    with open(path, "rb") as key_file:
        return serialization.load_pem_public_key(
            key_file.read(),
            backend=default_backend()
        )

def validate_key_pair(private_key, public_key):
    try:
        test_message = b"validasi_kunci_rsa_123"
        encrypted = public_key.encrypt(
            test_message,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        decrypted = private_key.decrypt(
            encrypted,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return decrypted == test_message
    except Exception as e:
        messagebox.showerror("Error", f"Validasi gagal: {str(e)}")
        return False

def run_validation():
    priv_path = private_key_entry.get()
    pub_path = public_key_entry.get()
    password = passphrase_entry.get()

    try:
        private_key = load_private_key(priv_path, password)
        public_key = load_public_key(pub_path)

        if validate_key_pair(private_key, public_key):
            messagebox.showinfo("Hasil Validasi", "✅ Kunci valid dan berpasangan!")
        else:
            messagebox.showwarning("Hasil Validasi", "❌ Kunci tidak cocok atau corrupt.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def browse_file(entry_field):
    filename = filedialog.askopenfilename(filetypes=[("PEM Files", "*.pem")])
    if filename:
        entry_field.delete(0, tk.END)
        entry_field.insert(0, filename)

# GUI setup
root = tk.Tk()
root.title("Validator RSA Key Pair")
root.geometry("500x250")

tk.Label(root, text="Private Key (.pem):").grid(row=0, column=0, sticky="e", padx=5, pady=5)
private_key_entry = tk.Entry(root, width=50)
private_key_entry.grid(row=0, column=1, padx=5, pady=5)
tk.Button(root, text="Browse", command=lambda: browse_file(private_key_entry)).grid(row=0, column=2, padx=5, pady=5)

tk.Label(root, text="Public Key (.pem):").grid(row=1, column=0, sticky="e", padx=5, pady=5)
public_key_entry = tk.Entry(root, width=50)
public_key_entry.grid(row=1, column=1, padx=5, pady=5)
tk.Button(root, text="Browse", command=lambda: browse_file(public_key_entry)).grid(row=1, column=2, padx=5, pady=5)

tk.Label(root, text="Passphrase (jika ada):").grid(row=2, column=0, sticky="e", padx=5, pady=5)
passphrase_entry = tk.Entry(root, show="*", width=50)
passphrase_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Button(root, text="Validasi Pasangan Kunci", command=run_validation, bg="green", fg="white").grid(row=3, column=1, pady=20)

root.mainloop()

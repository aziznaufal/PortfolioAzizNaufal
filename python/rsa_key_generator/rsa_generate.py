import tkinter as tk
from tkinter import filedialog, messagebox
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
import os
import subprocess
import tempfile

OPENSSL_PATH = "C:\\Program Files\\OpenSSL-Win64\\bin\\openssl.exe"

def encrypt_with_openssl(input_path, output_path, passphrase):
    try:
        result = subprocess.run(
        [
            OPENSSL_PATH, "pkcs8",
            "-topk8",
            "-in", input_path,
            "-out", output_path,
            "-passout", f"pass:{passphrase}",
            "-v1", "PBE-SHA1-3DES"
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
        )
        if result.returncode != 0:
            raise Exception(f"OpenSSL Error: {result.stderr.strip()}")
    except FileNotFoundError:
        raise Exception("OpenSSL not found. Make sure OpenSSL is installed and added to your system PATH.")

def generate_key():
    passphrase = passphrase_entry.get().encode()
    key_size = int(bit_entry.get())
    private_path = private_output_entry.get()
    public_path = public_output_entry.get()

    if not passphrase or not private_path or not key_size:
        messagebox.showerror("Error", "Field tidak boleh kosong.")
        return

    try:
        # 1. Generate private key
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=key_size,
            backend=default_backend()
        )

        # 2. Export to TEMP unencrypted PEM file (PKCS#8, No Encryption)
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pem") as tmpfile:
            tmpfile_path = tmpfile.name
            tmpfile.write(
                private_key.private_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PrivateFormat.PKCS8,
                    encryption_algorithm=serialization.NoEncryption()
                )
            )

        # 3. Encrypt using OpenSSL to DES-EDE3-CBC
        encrypt_with_openssl(tmpfile_path, private_path, passphrase.decode())

        # 4. Generate and save public key
        public_key = private_key.public_key()
        public_pem = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )

        if not public_path:
            public_path = private_path.replace(".pem", "_public.pem")

        with open(public_path, 'wb') as f:
            f.write(public_pem)

        # 5. Cleanup temp file
        os.remove(tmpfile_path)

        messagebox.showinfo("Sukses", f"Private Key disimpan di:\n{private_path}\n\nPublic Key disimpan di:\n{public_path}")

    except Exception as e:
        print(e)
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

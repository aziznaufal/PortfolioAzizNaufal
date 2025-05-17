# 🔐 RSA Encryption/Decryption Web App (Django)

A simple Django web application for securely encrypting and decrypting text using RSA public and private keys. This tool is ideal for learning about public-key cryptography and experimenting with RSA encryption in a web environment.

## 📌 Features

- RSA Key Pair generation (public/private)
- Encrypt plain text using a public key
- Decrypt cipher text using a private key
- Web-based interface built with Django
- Supports uploading custom keys or generating new ones

## 🛠️ Tech Stack

- Backend: [Django](https://www.djangoproject.com/)
- Frontend: HTML5, CSS3 (with optional Bootstrap)
- Encryption: Python's `cryptography` or `rsa` library
- Python version: 3.8+

## 📸 Preview


## 🚀 Getting Started

### 1. Clone the Repository

### 2. Create Virtual Environment and Install Dependencies

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Run Migrations

```bash
python manage.py migrate
```

### 4. Start the Development Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` to access the app.

## 📂 Project Structure

```
asymetric_rsa_encrypt_decrypt/
│
├── asymetric_rsa_encrypt_decrypt/ # Main Django Project setting
├── encryption/          # Main Django app
│   ├── templates/       # HTML templates
│   ├── static/          # Static files (CSS/JS)
│   ├── views.py         # Business logic
│   └── utils.py         # RSA helper functions
│
├── media/               # Uploaded key files (if any)
├── statis/              # Static folder for Script and style
├── manage.py
├── requirements.txt
└── README.md
```

## 🧪 Sample Use Cases

- Learn how RSA works
- Encrypt messages before sending over insecure channels
- Build secure communication features into Django apps

## ✅ TODO

- Add login/authentication (optional)
- Store keys securely in the database (optional)
- Add file encryption support (optional)
- Dockerize the app

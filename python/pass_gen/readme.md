# 🔐 Password Generator Web App (MVC + PyWebView)

A modern, lightweight **Password Generator** built with **pure Python, JavaScript, HTML/CSS** following the **MVC architectural pattern**, and packaged as a **windowed desktop app** using `pywebview`.

## ✨ Features

- ✅ Generate secure passwords with custom length and character sets  
- ✅ Built with **MVC (Model-View-Controller)** separation  
- ✅ Dynamic page routing with vanilla JavaScript (SPA-style navigation)  
- ✅ Modern "windowed app" UI using custom CSS  
- ✅ Packaged as a native window app using `pywebview`  
- ✅ Clean modular structure, ideal for scalability and maintenance  

## 🏗️ Project Structure

```
password_generator_web/
├── app.py                   # Entry point - starts server and desktop window
├── controller/
│   └── password_controller.py
├── model/
│   └── password_model.py
├── routes/
│   └── password_routes.py
├── view/
│   └── password_view.py
├── templates/
│   ├── base.html            # Main layout with dynamic content block
│   ├── home.html            # Home page content
│   └── generator.html       # Password generator form
├── static/
│   ├── style/
│   │   └── style.css        # Modern windowed-style styling
│   └── scripts/
│       └── app.js           # Routing and SPA behavior
```

## 🚀 How to Run

### 🧰 Requirements

- Python 3.8+
- pip packages:
  ```bash
  pip install flask pywebview
  ```

### ▶️ Launch the App

```bash
python app.py
```

This will:

1. Start a Flask-based server (without debug mode)
2. Launch a native desktop window pointing to `http://127.0.0.1:5000`

## 📷 Screenshots

![image](https://github.com/user-attachments/assets/338f63a9-0f5e-4ba5-bb8d-dc3eb0da69d6)

## 📦 Tech Stack

| Layer | Technology |
|-------|------------|
| View  | HTML, CSS, JavaScript (Vanilla) |
| Controller | Python (Flask routes) |
| Model | Custom Python logic |
| Window Shell | `pywebview` (Python-native GUI) |

## 🧠 What I Learned

- Structuring a Python web app using the **MVC pattern**
- Creating a lightweight **SPA-style** front-end without frameworks
- Integrating **Flask with PyWebView** for desktop deployment
- Handling asynchronous password generation and clipboard copying
- Building modular, maintainable codebases for desktop-ready web apps

## 📁 Future Improvements

- Add dark mode toggle  
- Allow saving password history  
- Export passwords to a file  
- Add strength meter and suggestions  

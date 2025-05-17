import time
import webview
from routes.routes import create_app
from threading import Thread

def main():
    app = create_app()

    def run_server():
        app.run(debug=False, use_reloader=False, port=5000)

    Thread(target=run_server, daemon=True).start()

    # Delay kecil biar server siap dulu
    time.sleep(1)  # coba 1 detik, sesuaikan jika perlu

    webview.create_window("Password Generator", "http://127.0.0.1:5000")
    webview.start()



if __name__ == "__main__":
    main()

import threading
import webview
import signal
import sys
from flask import Flask, render_template, request, url_for
from routes.weather_routes import weather_bp
from middleware.logger import request_logger
# from dotenv import load_dotenv
# load_dotenv()

# Initialize Flask app
app = Flask(__name__)
app.register_blueprint(weather_bp)
request_logger(app)

# Run Flask in a separate thread
def start_flask():
    app.run(debug=True, use_reloader=False, port=5000)  # Make sure to disable reloader when using threads

# Graceful shutdown function
def handle_shutdown(signum, frame):
    print("Shutting down...")
    webview.destroy()  # Close the webview window
    sys.exit(0)  # Exit the program

# Main entry point
if __name__ == '__main__':
    # Register signal handler to handle Ctrl+C (SIGINT)
    signal.signal(signal.SIGINT, handle_shutdown)
    print("Starting App")
    # Start Flask in a separate thread
    flask_thread = threading.Thread(target=start_flask)
    flask_thread.daemon = True  # Ensure it exits when the main thread exits
    flask_thread.start()

    # Open the webview as a desktop app
    webview.create_window("Weather Desktop App", "http://localhost:5000")

    # Wait until the window is closed (so that we don't block here)
    webview.start()

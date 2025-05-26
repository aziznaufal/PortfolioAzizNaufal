from flask import request
import datetime
import os

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "access.log")

def register_middleware(app):
    @app.before_request
    def log_request():
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_message = f"[{timestamp}] {request.method} {request.path}"

        print(log_message)  # still print to console

        # Write to file
        os.makedirs(LOG_DIR, exist_ok=True)
        with open(LOG_FILE, "a") as f:
            f.write(log_message + "\n")

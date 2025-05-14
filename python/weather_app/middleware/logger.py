from flask import request
import logging


def request_logger(app):
    @app.before_request
    def log_request_info():
        print(f"[Request] {request.method} {request.path}")

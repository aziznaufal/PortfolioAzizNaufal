from flask import Flask, render_template, request, jsonify
from controller.controller import PasswordController

def create_app():
    app = app = Flask(__name__, template_folder='../templates', static_folder='../static')
    controller = PasswordController()

    @app.route("/")
    def home():
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            # Jika request AJAX, render partial tanpa extend base.html
            return render_template("home_content.html")
        else:
            # Jika direct akses browser, render full page dengan base.html
            return render_template("home.html")

    @app.route("/generator")
    def generator():
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return render_template("generator_content.html")
        else:
            return render_template("generator.html")

    @app.route("/api/generate_password", methods=["POST"])
    def generate_password():
        data = request.json
        length = data.get("length")
        use_upper = data.get("use_upper")
        use_lower = data.get("use_lower")
        use_digits = data.get("use_digits")
        use_symbols = data.get("use_symbols")

        try:
            password = controller.generate_password(length, use_upper, use_lower, use_digits, use_symbols)
            return jsonify({"password": password})
        except Exception as e:
            return jsonify({"error": str(e)}), 400

    return app

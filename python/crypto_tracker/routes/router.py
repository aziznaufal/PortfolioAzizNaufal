from flask import render_template, jsonify, request
from controller.coin_controller import get_all_coins, add_coin
from middleware.validator import validate_json

def setup_routes(app):
    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/api/prices", methods=["GET"])
    def get_prices():
        return jsonify(get_all_coins())

    @app.route("/api/prices", methods=["POST"])
    @validate_json(["name", "symbol", "price", "change_24h"])
    def post_price():
        # Use the validated and cleaned data
        coin_data = request.validated_json
        result, status = add_coin(coin_data)
        return jsonify(result), status

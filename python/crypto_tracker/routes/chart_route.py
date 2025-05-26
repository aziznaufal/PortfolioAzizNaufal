from flask import Blueprint, request, jsonify
from controller.chart_controller import search_coins, get_chart_data, get_coin_kline, get_price

chart_route = Blueprint("chart_route", __name__)

@chart_route.route("/api/search")
def api_search():
    query = request.args.get("q", "")
    return jsonify(search_coins(query))

@chart_route.route("/api/chart")
def api_chart():
    symbol = request.args.get("symbol")
    chart_type = request.args.get("type", "line")
    interval = request.args.get("interval", "1m")

    if not symbol:
        return jsonify({"error": "Missing symbol"}), 400

    data = get_chart_data(symbol, chart_type, interval)
    return jsonify(data)

@chart_route.route('/api/kline')
def kline():
    symbol = request.args.get('symbol')
    interval = request.args.get('interval', '1m')
    return jsonify(get_coin_kline(symbol, interval))

@chart_route.route('/api/price')
def price():
    symbol = request.args.get('symbol')
    return jsonify(get_price(symbol))
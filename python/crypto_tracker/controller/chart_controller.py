from model.binance_model import fetch_symbols, fetch_ohlc
from dto.coin_dto import CoinDTO
from dto.chart_dto import ChartDTO
import requests
from dto.coin_chart_dto import transform_kline_data
from model.coin_model import BinanceModel

def search_coins(query):
    query = query.lower()
    all_symbols = fetch_symbols()
    matched = [
        CoinDTO(sym["symbol"], sym["baseAsset"], sym["quoteAsset"])
        for sym in all_symbols
        if query in sym["baseAsset"].lower()
    ]
    return [coin.to_dict() for coin in matched[:10]]

def get_chart_data(symbol, chart_type="line", interval="1m"):
    raw = fetch_ohlc(symbol, interval)
    formatted = ChartDTO.format(raw, chart_type)
    return {
        "data": formatted,
        "type": chart_type
    }

def get_coin_kline(symbol, interval):
    raw_data = BinanceModel.fetch_kline(symbol, interval)
    return transform_kline_data(raw_data)

def get_price(symbol):
    return BinanceModel.fetch_current_price(symbol)
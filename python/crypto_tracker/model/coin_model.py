import json
from dto.coin_dto import CoinDTO
import os

DATA_FILE = os.path.join(os.path.dirname(__file__), "../data/coins.json")

def read_coins():
    with open(DATA_FILE, "r") as f:
        data = json.load(f)
        return [CoinDTO(**coin) for coin in data]

def write_coins(coins):
    with open(DATA_FILE, "w") as f:
        json.dump([coin.to_dict() for coin in coins], f, indent=2)

import requests

class BinanceModel:
    BASE_URL = 'https://api.binance.com/api/v3'

    @staticmethod
    def fetch_kline(symbol, interval):
        url = f"{BinanceModel.BASE_URL}/klines"
        params = {'symbol': symbol.upper(), 'interval': interval, 'limit': 100}
        res = requests.get(url, params=params)
        return res.json()

    @staticmethod
    def fetch_current_price(symbol):
        url = f"{BinanceModel.BASE_URL}/ticker/price"
        params = {'symbol': symbol.upper()}
        res = requests.get(url, params=params)
        return res.json()

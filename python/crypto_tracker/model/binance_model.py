import requests

def fetch_symbols():
    res = requests.get("https://api.binance.com/api/v3/exchangeInfo")
    print("after get")
    return res.json()["symbols"] if res.status_code == 200 else []

def fetch_ohlc(symbol, interval="1m", limit=100):
    url = f"https://api.binance.com/api/v3/klines?symbol={symbol}&interval={interval}&limit={limit}"
    res = requests.get(url)
    return res.json() if res.status_code == 200 else []

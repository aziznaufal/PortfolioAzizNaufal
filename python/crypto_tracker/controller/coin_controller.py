from model.coin_model import read_coins, write_coins
from dto.coin_dto import CoinDTO

def get_all_coins():
    coins = read_coins()
    return [coin.to_dict() for coin in coins]

def add_coin(coin_data):
    coins = read_coins()

    # Check for duplicate symbol
    if any(c.symbol == coin_data['symbol'] for c in coins):
        return {"error": "Coin with this symbol already exists"}, 400

    new_coin = CoinDTO(**coin_data)
    coins.append(new_coin)
    write_coins(coins)
    return {"message": "Coin added successfully"}, 201

import json
import os
from dto.transaction_dto import TransactionDTO

DATA_FILE = 'data/transactions.json'

def load_transactions():
    if not os.path.exists(DATA_FILE):
        return []

    with open(DATA_FILE, 'r') as file:
        try:
            data = json.load(file)
            return [TransactionDTO.from_dict(d) for d in data]
        except json.JSONDecodeError:
            return []

def save_transaction(new_txn):
    transactions = load_transactions()
    transactions.append(new_txn)
    with open(DATA_FILE, 'w') as file:
        json.dump([t.to_dict() for t in transactions], file, indent=2)

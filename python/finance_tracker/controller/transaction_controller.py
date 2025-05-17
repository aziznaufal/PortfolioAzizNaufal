from flask import Blueprint, request, jsonify
from model.transaction_model import load_transactions, save_transaction
from dto.transaction_dto import TransactionDTO

transaction_api = Blueprint('transaction_api', __name__)

@transaction_api.route('/api/transactions', methods=['GET'])
def get_transactions():
    txns = load_transactions()
    return jsonify([txn.to_dict() for txn in txns])

@transaction_api.route('/api/transactions', methods=['POST'])
def post_transaction():
    data = request.json
    txn = TransactionDTO.from_dict(data)
    save_transaction(txn)
    return jsonify({"message": "Transaction saved!"}), 201

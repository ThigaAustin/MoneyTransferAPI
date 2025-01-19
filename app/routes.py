from flask import Blueprint, jsonify, request
from app.models import Account, Transfer
from app.database import db

bp = Blueprint('routes', __name__)

@bp.route('/accounts', methods=['POST'])
def create_account():
    data = request.json
    name = data.get('name')
    balance = data.get('balance', 0.0)

    if balance < 0:
        return jsonify({'error': 'Balance cannot be negative. Please try again'}), 400

    account = Account(name=name, balance=balance)
    db.session.add(account)
    db.session.commit()
    return jsonify({'id': account.id, 'name': account.name, 'balance': account.balance}), 201

@bp.route('/accounts/<int:id>', methods=['GET'])
def get_account(id):
    account = Account.query.get(id)
    if not account:
        return jsonify({'error': 'Account not found, try a valid  account ID'}), 404
    return jsonify({'id': account.id, 'name': account.name, 'balance': account.balance})

@bp.route('/transfers', methods=['POST'])
def transfer_money():
    data = request.json
    source_id = data.get('source_account_id')
    target_id = data.get('target_account_id')
    amount = data.get('amount', 0.0)

    if amount <= 0:
        return jsonify({'error': 'Transfer amount must be greater than zero'}), 400

    source_account = Account.query.get(source_id)
    target_account = Account.query.get(target_id)

    if not source_account or not target_account:
        return jsonify({'error': 'Invalid account(s)'}), 404

    if source_account.balance < amount:
        return jsonify({'error': 'Insufficient funds, Top up and Try again'}), 400

    # Perform the transfer
    source_account.balance -= amount
    target_account.balance += amount

    # Save the transfer record
    transfer = Transfer(source_account_id=source_id, target_account_id=target_id, amount=amount)
    db.session.add(transfer)
    db.session.commit()

    return jsonify({'message': 'Transfer successful'})

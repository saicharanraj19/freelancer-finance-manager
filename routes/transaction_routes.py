from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.transaction import get_transaction_collection

bp = Blueprint('transactions', __name__, url_prefix='/api/transactions')

@bp.route('/', methods=['POST'])
@jwt_required()
def add_transaction():
    data = request.get_json()
    current_user = get_jwt_identity()
    transaction = {
        'userId': current_user['username'],
        'type': data['type'],
        'amount': data['amount'],
        'category': data['category'],
        'date': data['date']
    }
    get_transaction_collection().insert_one(transaction)
    return jsonify({"msg": "Transaction added"}), 201

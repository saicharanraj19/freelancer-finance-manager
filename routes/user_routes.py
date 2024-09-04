from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from models.user import get_user_collection

bp = Blueprint('users', __name__, url_prefix='/api/users')

@bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']
    # Validate user credentials
    user = get_user_collection().find_one({'username': username, 'password': password})
    if user:
        access_token = create_access_token(identity={'username': username})
        return jsonify(access_token=access_token)
    return jsonify({"msg": "Invalid credentials"}), 401

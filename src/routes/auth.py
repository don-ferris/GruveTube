from flask import Blueprint, request, jsonify
from werkzeug.security import check_password_hash
from src.models import User

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({'error': 'Missing username or password'}), 400

    username = data['username']
    password = data['password']

    user = User.query.filter_by(username=username).first()
    if not user or not check_password_hash(user.password_hash, password):
        return jsonify({'error': 'Invalid credentials'}), 401

    return jsonify({'message': 'Login successful', 'user': username}), 200

@auth_bp.route('/logout', methods=['POST'])
def logout():
    return jsonify({'message': 'Logout successful'}), 200

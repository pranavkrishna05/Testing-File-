from flask import Blueprint, jsonify, request
from app.repositories.user_repository import UserRepository
from app.models.user import User

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id: int):
    user = UserRepository.get_user_by_id(user_id)
    if user:
        return jsonify({ 'id': user.id, 'username': user.username, 'email': user.email })
    else:
        return jsonify({ 'error': 'User not found' }), 404

@user_bp.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    user = User(username=data['username'], email=data['email'])
    UserRepository.add_user(user)
    return jsonify({ 'message': 'User added successfully' }), 201

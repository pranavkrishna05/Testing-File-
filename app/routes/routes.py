from flask import Blueprint, request, jsonify
from app.services.user_service import UserService

api_bp = Blueprint('api', __name__)
user_service = UserService()

@api_bp.route('/register', methods=['POST'])
def register():
    data = request.json

    if not data:
        return jsonify({"error": "Invalid input."}), 400

    try:
        user = user_service.register_user(data)
        return jsonify(user), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

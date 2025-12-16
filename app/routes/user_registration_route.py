from flask import Blueprint, request, jsonify
from app.services.user_registration_service import register_user

user_registration_bp = Blueprint('user_registration', __name__)

@user_registration_bp.route('/register', methods=['POST'])
def register():
    """
    Handle user registration.
    Expects a JSON payload with 'email' and 'password'.
    """
    try:
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')
        if not email or not password:
            return jsonify({
                'success': False,
                'message': 'Email and password are required.'
            }), 400

        response = register_user(email, password)
        return jsonify(response), response['status_code']

    except Exception as e:
        return jsonify({
            'success': False,
            'message': 'An error occurred during registration.',
            'error': str(e)
        }), 500
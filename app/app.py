from flask import Flask
from app.routes.routes import api_bp
from app.config.config import get_config
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] - %(message)s'
)

def create_app(env: str = 'development') -> Flask:
    """
    Factory function to create and configure the Flask application.

    Args:
        env (str): The application environment ('development', 'testing', 'production').

    Returns:
        Flask: Configured Flask application instance.
    """
    app = Flask(__name__)

    # Load environment-specific configuration
    app.config.from_object(get_config(env))

    # Register blueprints
    app.register_blueprint(api_bp, url_prefix='/api')

    @app.route('/health', methods=['GET'])
    def health_check():
        return {"status": "healthy"}, 200

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000)

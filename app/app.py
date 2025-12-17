import os
from flask import Flask
from app.config import configure_app
from app.routes import register_routes
from app.models import db

app = Flask(__name__)

# Configure the app
configure_app(app)

# Initialize database
db.init_app(app)

# Register routes
register_routes(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=os.environ.get('DEBUG', 'False').lower() in ['true', '1', 't'])

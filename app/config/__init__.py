from flask import Flask
from .config import DevelopmentConfig, ProductionConfig
import os

def configure_app(app: Flask):
    env = os.environ.get('FLASK_ENV', 'development')
    if env == 'production':
        app.config.from_object(ProductionConfig)
    else:
        app.config.from_object(DevelopmentConfig)

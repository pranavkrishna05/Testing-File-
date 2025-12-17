import os

class Config{
    SECRET_KEY = os.environ.get('SECRET_KEY', 'default_secret')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///default.db')
    DEBUG = os.environ.get('DEBUG', 'False').lower() in ['true', '1', 't']

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

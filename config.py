import os
from dotenv import load_dotenv

# Load environment variables from .env file

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    MODEL_PATH = os.getenv('MODEL_PATH', 'models/model.joblib')

@staticmethod
def init_app(app):
    """Initialize the app with additional configurations.""" 
    pass

class DevelopmentConfig(Config):
    DEBUG=True
    FLASK_ENV='development'

class ProductionConfig(Config):
    DEBUG=False
    FLASK_ENV = 'production'

# Dictionary to map environment  to respective config class
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'defualt': DevelopmentConfig
}
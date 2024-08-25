import os
from dotenv import load_dotenv

# Load environment variables from .env file

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'defualt_secret_key')
    MODEL_PATH = os.getenv('MODEL_PATH', 'models/model.joblib')
    
class DevelopmentConfig(Config):
    DEBUG=True

class ProductionConfig(Config):
    DEBUG=False
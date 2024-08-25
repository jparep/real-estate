import os
from dotenv import load_dotenv

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'defualt_secret_key')
    MODEL_PATH = os.getenv('MODEL_PATH', 'models/model.joblib')
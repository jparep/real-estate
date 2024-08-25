import os
from app import create_app

# Determine the environment from an environment variable, with 'production' as the default
config_name = os.getenv('FLASK_CONFIG', 'production')
app = create_app(config_name)

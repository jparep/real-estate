import os
from app import create_app

# Determine hte environment from an environment variable, with 'production' as the default
app = os.getenv('FLASK_CONFIG', 'production')
app = create_app(config_name)
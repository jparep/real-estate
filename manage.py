import os
from flask import Flask
from app import create_app

# Determine the environment from an environment variable, with 'production' as the default
config_name = os.getenv('FLASK_CONFIG', 'production')
app = create_app(config_name)

if __name__ == '__main__':
    # Run the Flask application
    app.run()

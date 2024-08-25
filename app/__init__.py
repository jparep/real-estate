import os
from dotenv import load_dotenv
from flask import Flask
from config import config  # This should refer to the `config` dictionary, not `Config`

def create_app(config_name=None):
    if config_name is None:
        config_name = os.getenv('FLASK_ENV', 'development')
        
    app = Flask(__name__)
    
    # Load the appropriate configuration
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    
    # Register your routes, blueprints, etc.
    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    return app

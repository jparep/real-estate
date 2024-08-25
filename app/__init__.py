from flask import Flask
from config import Config

def create_app(config_name='defualt'):
    app= Flask(__name__)
    
    # Load the appropriate configuration
    app.config.from_object(Config[config_name])
    Config[config_name].init_app(app)
    
    # REgister your routes, blueprints, etc
    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    return app

import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import create_app, db  # Ensure you import the `db` object from your models

# Determine the environment from an environment variable, with 'production' as the default
config_name = os.getenv('FLASK_CONFIG', 'production')
app = create_app(config_name)

# Initialize Flask-Script manager
manager = Manager(app)

# Initialize Flask-Migrate
migrate = Migrate(app, db)

# Add Flask-Migrate commands to the manager
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    # Run the manager with the specified commands
    manager.run()

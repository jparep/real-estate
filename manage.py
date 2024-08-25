from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from app import create_app, db  # Ensure you import the `db` object from your models

config_name = os.getenv('FLASK_CONFIG', 'production')
app = create_app(config_name)

manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()

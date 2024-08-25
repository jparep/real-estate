from flask_script import Manager
from app import create_app

# Specify the environment configuration
app = create_app('production')

manager = Manager(app)

if __name__=='__main__':
    manager.run()
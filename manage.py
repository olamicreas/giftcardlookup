
from app import app

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

migrate = Migrate(app)
manager = Manager(app)

manager.add_command(MigrateCommand)

if __name__ == '__main__':
    manager.run()

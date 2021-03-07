from flask_migrate import Migrate
from inventory_control.ext.db import db

migrate = Migrate(db=db)


def init_app(app):
    migrate.init_app(app=app)

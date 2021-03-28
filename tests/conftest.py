import pytest
from inventory_control.app import create_app
from inventory_control.ext.db import db


@pytest.fixture(scope="session")
def app():
    app = create_app(FORCE_ENV_FOR_DYNACONF="testing")
    with app.app_context():
        db.create_all(app=app)
        yield app
        db.session.remove()
        db.drop_all(app=app)
    return app

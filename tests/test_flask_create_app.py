from inventory_control.app import create_app
from flask import Flask


def test_create_app_return_flask(app):
    assert isinstance(app, Flask)

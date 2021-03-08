from flask import Flask
from dynaconf import FlaskDynaconf


def create_app(**config):
    app = Flask(__name__)
    FlaskDynaconf(app, extensions_list="EXTENSIONS", **config)
    return app

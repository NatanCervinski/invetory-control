from flask_restful import Api

api = Api()


def init_app(app):
    api.init_app(app)

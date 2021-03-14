from flask_restful import Api
from .resources.product import ProductRegister

api = Api()


def init_app(app):
    api.add_resource(ProductRegister, "/product")
    api.init_app(app)

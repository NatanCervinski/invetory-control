from flask_restful import Api
from .resources.user import UserRegister, Login
from .resources.product import ProductRegister, Product

api = Api()


def init_app(app):
    api.add_resource(UserRegister, "/user_register")
    api.add_resource(Login, "/login")

    api.add_resource(ProductRegister, "/product")
    api.add_resource(Product, "/product/<int:id>")
    api.init_app(app)

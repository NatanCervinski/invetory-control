from flask import request
from flask_restful import Resource
from inventory_control.ext.serialization.schemas.product import (
    ProductSchema,
)
from inventory_control.ext.serialization.schemas.product import (
    ProductModel,
)
from inventory_control.ext.db.database_commands import DatabaseCommands
from marshmallow.exceptions import ValidationError

product_schema = ProductSchema()


class ProductRegister(Resource):
    def post(self):
        product_json = request.get_json()
        try:
            product = product_schema.load(product_json)
        except ValidationError as e:
            return {"error": e.messages}
        product_database = ProductModel.find_by_id(
            product_schema.dump(product)["id"]
        )
        if product_database:
            return {"message": "Id already exists"}, 409
        try:
            DatabaseCommands.insert_into_database(product)
        except Exception as e:
            return e
        return {"message": "Success"}, 201


class Product(Resource):
    def get(self, id):
        product_json = ProductModel.find_by_id(id)
        if not product_json:
            return {"message": "Product not found"}, 404
        product = product_schema.dump(product_json)
        return product, 200

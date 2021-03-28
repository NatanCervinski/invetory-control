from flask import request
from flask_restful import Resource
from inventory_control.ext.serialization.schemas.product import (
    ProductSchema,
)
from inventory_control.ext.serialization.schemas.product import (
    ProductModel,
)
from inventory_control.ext.db.database_commands import DatabaseCommands

product_schema = ProductSchema()


class ProductRegister(Resource):
    def post(self):
        product_json = request.get_json()
        product = product_schema.load(product_json)
        DatabaseCommands.insert_into_database(product)
        return {"message": "Success"}, 201


class Product(Resource):
    def get(self, id):
        product_json = ProductModel.find_by_id(id)
        product = product_schema.dump(product_json)
        return product, 200

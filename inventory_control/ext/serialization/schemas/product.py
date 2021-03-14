from inventory_control.ext.serialization import ma
from inventory_control.ext.db.models.product import ProductModel
from inventory_control.ext.db import db


class ProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ProductModel
        sqla_session = db.session
        load_instance = True

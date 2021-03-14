from inventory_control.ext.serialization import ma
from inventory_control.ext.db.models.product import ProductModel


class ProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ProductModel

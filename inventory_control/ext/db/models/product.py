from inventory_control.ext.db import db


class ProductModel(db.Model):
    __tablename__ = "product"

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float())

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

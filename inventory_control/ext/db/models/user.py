from inventory_control.ext.db import db


class UserModel(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer(), primary_key=True)
    user = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(100), nullable=False)

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_by_user(cls, user):
        return cls.query.filter_by(user=user).first()

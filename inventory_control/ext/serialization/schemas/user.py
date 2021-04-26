from inventory_control.ext.serialization import ma
from inventory_control.ext.db.models.user import UserModel
from inventory_control.ext.db import db
from flask_marshmallow.fields import fields


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = UserModel
        sqla_session = db.session
        load_instance = True
        dump_only = ["id"]


class LoginSchema(ma.Schema):
    user = fields.Str()
    password = fields.Str()

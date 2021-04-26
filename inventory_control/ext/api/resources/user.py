from flask import request, jsonify
from flask_restful import Resource
from flask_jwt_extended import create_access_token, jwt_required
from inventory_control.ext.serialization.schemas.user import (
    UserSchema,
    LoginSchema,
)
from inventory_control.ext.db.models.user import (
    UserModel,
)
from inventory_control.ext.db.database_commands import DatabaseCommands
from marshmallow.exceptions import ValidationError
from werkzeug.security import safe_str_cmp

user_schema = UserSchema()
login_schema = LoginSchema()


class UserRegister(Resource):
    @jwt_required()
    def post(self):
        user_json = request.get_json()
        try:
            user = user_schema.load(user_json)
        except ValidationError as e:
            return {"error": e.messages}, 400
        user_database = UserModel.find_by_user(
            user_schema.dump(user)["user"]
        )
        if user_database:
            return {"message": "User already exists"}, 409
        try:
            DatabaseCommands.insert_into_database(user)
        except Exception as e:
            return e, 500
        return {"message": "Success"}, 201


class Login(Resource):
    def post(self):
        login_json = request.get_json()
        try:
            login = login_schema.load(login_json)
        except ValidationError as e:
            return {"error": e.messages}, 400
        user_database = UserModel.find_by_user(
            login_schema.dump(login)["user"]
        )
        if not user_database:
            return {"error": "User or password incorrect"}, 401
        if safe_str_cmp(
            login_schema.dump(login)["password"],
            user_database.password,
        ):
            access_token = create_access_token(
                identity=user_database.user
            )
            return jsonify(access_token=access_token)
        else:
            return {"error": "User or password incorrect"}, 401

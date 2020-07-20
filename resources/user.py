import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type=str,
        required=True,
        help="This cannot be left blank."
    )
    parser.add_argument('password',
        type=str,
        required=True,
        help="Incorrect password."
    )

    def post(self):
        data = UserRegister.parser.parse_args()

        # The following checks if a user with the username entered exists
        if UserModel.find_by_username(data['username']):
            return {"message": "A user with that username exists!"}, 400

        user = UserModel(**data)
        user.save_to_db()
        return {"message": "User successfully created."}, 201

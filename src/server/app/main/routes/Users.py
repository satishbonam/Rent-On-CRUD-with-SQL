from flask import Flask, request
from flask_restful import Resource, reqparse
from app.main import db
from app.main.services.users import user_registration


class UserRegistration(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, required=True)
    parser.add_argument('email', type=str, required=True)
    parser.add_argument('mobile', type=str, required=True)
    parser.add_argument('password', type=str, required=True)
    parser.add_argument('role', type=str, required=True)

    @classmethod
    def post(self):
        data = UserRegistration.parser.parse_args()
        flag_request, msg = user_registration(data)

        if flag_request:
            return {'status': True, 'msg': msg}
        else:
            return {'status': False, 'msg': msg}

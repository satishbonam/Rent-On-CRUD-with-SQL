from flask import Flask, request
from flask_restful import Resource, reqparse
from app.main import db
import jwt
from app.main.services.authentication import user_login


class Login(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('email', type=str, required=True)
    parser.add_argument('password', type=str, required=True)

    @classmethod
    def post(self):
        data = Login.parser.parse_args()
        flag_request, token = user_login(data)

        if flag_request:
            return {'status': True, 'msg': "Successfull", 'token': token}
        else:
            return {'status': False, 'msg': "Incorrect Credentials"}


class Logout(Resource):

    @classmethod
    def get(self):
        return {'status': True, 'msg': "Successfull", 'token': ""}

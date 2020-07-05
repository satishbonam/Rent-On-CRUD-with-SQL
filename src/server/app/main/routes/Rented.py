from flask import Flask, request
from flask_restful import Resource, reqparse
from app.main import db
from app.main.services.rented import property_rented
from app.main.utils.validate_user import validate_user


class Rented(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('property_id', type=int, required=True)

    @classmethod
    def post(self):
        auth_token = request.headers.get('token')
        data = Rented.parser.parse_args()

        flag_validate, token_data = validate_user(auth_token)

        if flag_validate and token_data['role'] in ['user', 'admin', 'owner']:
            flag_request = property_rented(data, token_data['id'])
            if flag_request:
                return {'status': True, 'msg': "Property Rented successfully"}
            else:
                return {'status': False, 'msg': "request unsuccessfull"}
        elif flag_validate:
            return {'status': False, 'msg': "access denied"}
        else:
            return {'status': False, 'msg': "invalid token"}

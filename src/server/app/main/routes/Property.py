from flask import Flask, request
from flask_restful import Resource, reqparse
from app.main import db
from app.main.utils.validate_user import validate_user
from app.main.services.property import create_property, delete_property, edit_property, get_properties_all


class Property(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('area', type=str, required=True)
    parser.add_argument('bedrooms', type=str, required=True)
    parser.add_argument('furnishing', type=bool, required=False, default=False)
    parser.add_argument('locality', type=str, required=True)
    parser.add_argument('isRented', type=bool, required=False, default=False)
    parser.add_argument('amenitines', type=dict, required=True, default={})

    @classmethod
    def post(self):
        auth_token = request.headers.get("token")
        data = Property.parser.parse_args()

        flag_validate, token_data = validate_user(auth_token)
        data['owner_id'] = token_data['id']

        if flag_validate and token_data['role'] in ['owner', 'admin']:
            flag_request = create_property(data)
            if flag_request:
                return {'status': True, 'msg': "Property Added successfully"}
            else:
                return {'status': False, 'msg': "request unsuccessfull"}
        elif flag_validate:
            return {'status': False, 'msg': "access denied"}
        else:
            return {'status': False, 'msg': "invalid token"}

    @classmethod
    def get(self):
        auth_token = request.headers.get("token")
        flag_validate, token_data = validate_user(auth_token)

        if flag_validate and token_data['role'] in ['owner', 'admin', 'user']:
            flag_request, data = get_properties_all()
            if flag_request:
                return {'status': True, 'msg': 'Successfull', 'properties_data': data}
            else:
                return {'status': False, 'msg': "request unsuccessfull"}
        elif flag_validate:
            return {'status': False, 'msg': "access denied"}
        else:
            return {'status': False, 'msg': "invalid token"}


class EditProperty(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('property_id', type=int, required=True)
    parser.add_argument('area', type=str, required=True)
    parser.add_argument('bedrooms', type=str, required=True)
    parser.add_argument('furnishing', type=bool, required=False, default=False)
    parser.add_argument('locality', type=str, required=True)
    parser.add_argument('isRented', type=bool, required=False, default=False)
    parser.add_argument('amenitines', type=dict, required=True, default={})

    @classmethod
    def post(self):
        auth_token = request.headers.get("token")
        data = EditProperty.parser.parse_args()

        flag_validate, token_data = validate_user(auth_token)

        if flag_validate and token_data['role'] in ['owner', 'admin']:
            flag_request = edit_property(data, token_data['id'])
            if flag_request:
                return {'status': True, 'msg': "Property Updated successfully"}
            else:
                return {'status': False, 'msg': "request unsuccessfull"}
        elif flag_validate:
            return {'status': False, 'msg': "access denied"}
        else:
            return {'status': False, 'msg': "invalid token"}


class DeleteProperty(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('property_id', type=int, required=True)

    @classmethod
    def post(self):
        auth_token = request.headers.get("token")
        data = DeleteProperty.parser.parse_args()

        flag_validate, token_data = validate_user(auth_token)

        if flag_validate and token_data['role'] in ['owner', 'admin']:
            flag_request = delete_property(data, token_data['id'])
            if flag_request:
                return {'status': True, 'msg': "Property Deleted successfully"}
            else:
                return {'status': False, 'msg': "request unsuccessfull"}
        elif flag_validate:
            return {'status': False, 'msg': "access denied"}
        else:
            return {'status': False, 'msg': "invalid token"}

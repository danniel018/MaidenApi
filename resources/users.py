from flask import request
from flask_restful import Resource
from http import HTTPStatus
from models.albums import Users   
from schemas.members import UsersSchema
from marshmallow import ValidationError

users_schema = UsersSchema()

class NewUser(Resource):

    def post(self):
    
        json_data = request.get_json()

        try: 
            data = users_schema.load(data=json_data)

        except ValidationError as e:
            return e.messages,HTTPStatus.BAD_REQUEST
        
        if Users.get_by_email(data.get('mail')):
            return {'message': 'email already used'}, HTTPStatus.BAD_REQUEST

        user = Users(**data)
        user.save() 

        return users_schema.dump(user), HTTPStatus.CREATED



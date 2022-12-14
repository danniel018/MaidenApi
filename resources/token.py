from http import HTTPStatus
from flask import request
from flask_restful import Resource
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    get_jwt_identity,
    jwt_required,
    get_jwt
    
    
)

from werkzeug.security import check_password_hash

from models.albums import Users

block_list = set()


class Token(Resource):

    def post(self):

        json_data = request.get_json()

        mail = json_data.get('mail')
        password = json_data.get('password') 

        user = Users.get_by_email(mail=mail)

        if not user or not check_password_hash(user.password,password):
            return {'message': 'username or password is incorrect'}, HTTPStatus.UNAUTHORIZED
        
        user_name = {'name':user.name}
        access_token = create_access_token(identity=user.user_id, additional_claims=user_name, fresh=True)
        refresh_token = create_refresh_token(identity=user.user_id)

        return {'access_token': access_token, 'refresh_token': refresh_token}, HTTPStatus.OK 

class RefreshToken(Resource):

    @jwt_required(refresh=True)
    def post(self):
        current_user = get_jwt_identity()

        token = create_access_token(identity=current_user, fresh=False)
        return {'token': token}, HTTPStatus.OK

class RevokeToken(Resource):

    @jwt_required()
    def post(self):
        
        jti = get_jwt()['jti']
        block_list.add(jti) 
        #vt_1P__SioINRwsb2CAEv2zo63TEROte3Gzh
        
        return {'message': 'Successfully logged out'}, HTTPStatus.OK
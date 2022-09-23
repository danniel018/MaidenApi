from unicodedata import name
from flask import request
from flask_restful import Resource
from http import HTTPStatus
from models.members import Members      
from schemas.members import MembersSchema
from marshmallow import ValidationError

all_members_schema = MembersSchema(many=True,exclude=('songs','periods','albums')) 
member_schema = MembersSchema(exclude=('member_id',))


class MaidenMembers(Resource):

    def get(self):
        
        members = Members.all_members()  
        return all_members_schema.dump(members),HTTPStatus.OK

    def post(self): ##post method is written in this class due to no id is needed to upload a resource unlike the class Member
        
        member_data = request.get_json() 
        
        try:
            data = all_members_schema.load(data=member_data)
        except ValidationError as e:
            print(e.messages)
            return e.messages,HTTPStatus.BAD_REQUEST

        new_member=Members(**data)
        new_member.save()

        return all_members_schema.dump(new_member), HTTPStatus.CREATED

class Member(Resource):
    
    def get(self,id):

        member = Members.member_by_id(id)

        if member == None:
            return {'data':'not found that'},HTTPStatus.NOT_FOUND 

        return member_schema.dump(member), HTTPStatus.OK


    def put(self,id):
        member_data = request.get_json()

        try:
            deserialized_data = member_schema.load(data=member_data)
        except ValidationError as e:
            return e.messages,HTTPStatus.BAD_REQUEST

        member = Members.member_by_id(id)

        if member == None:
            return {'data':'not found that'},HTTPStatus.NOT_FOUND 



        member.name=deserialized_data.get('name')
        member.date_of_birth = deserialized_data.get('date_of_birth')
        member.active=deserialized_data.get('active')

        member.save()

        return member_schema.dump(member),HTTPStatus.OK
    
    
    def delete(self,id):

        member = Members.member_by_id(id)

        if member == None:
            return {'data':'not found that'},HTTPStatus.NOT_FOUND 

        member.delete()

        return {'data':'resource deleted succesfully'}, HTTPStatus.NO_CONTENT
         
                
        
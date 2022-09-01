from unicodedata import name
from flask import request
from flask_restful import Resource
from http import HTTPStatus
from models.members import Members      

class MaidenMembers(Resource):

    def get(self):
        
        members = Members.all_members()
        data=[x.queried_data() for x in members]
            
        return data,HTTPStatus.OK

    def post(self): ##post method is written in this class due to no id is needed to upload a resource unlike the class Member
        member_data = request.get_json()
        new_member = Members(name=member_data['name'], 
            date_of_birth=member_data['birthday'],
            active=member_data['active'])
        
        new_member.save()

        return new_member.queried_data(), HTTPStatus.CREATED

class Member(Resource):
    
    def get(self,id):

        member = Members.member_by_id(id)

        if member == None:
            return {'data':'not found that'},HTTPStatus.NOT_FOUND 

        return member.queried_data(), HTTPStatus.OK


    def put(self,id):
        member_data = request.get_json()
        member = Members.member_by_id(id)

        if member == None:
            return {'data':'not found that'},HTTPStatus.NOT_FOUND 
    
        member.name=member_data['name']
        member.date_of_birth = member_data['birthday']
        member.active=member_data['active']

        member.save()

        return member.queried_data(),HTTPStatus.OK
    
    
    def delete(self,id):

        member = Members.member_by_id(id)

        if member == None:
            return {'data':'not found that'},HTTPStatus.NOT_FOUND 

        member.delete()

        return {'data':'resource deleted succesfully'}, HTTPStatus.NO_CONTENT
         
                
        
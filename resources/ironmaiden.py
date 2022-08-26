from flask import request
from flask_restful import Resource
from http import HTTPStatus
from models.ironmaiden import Members

class MaidenMembers(Resource):

    def get(self):
        data=[]
        members = Members.all_members()
        for x in members:
            member_info={}
            member_info['name'] = x.name 
            data.append(member_info)
        return data,HTTPStatus.OK

# class Members(Resource):
#     def get(self,id):

#         for x in members:
#             if id == x['id']:
#                 member = x
#                 return member,HTTPStatus.OK
                
#         return {'data':'not found that'},HTTPStatus.NOT_FOUND 
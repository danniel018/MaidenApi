from ast import dump
from re import T
from typing import Type
from marshmallow import Schema, fields, validate, post_dump
from werkzeug.security import generate_password_hash
from datetime import datetime


class MembersSchema(Schema):
    class Meta:
        ordered = True
    member_id = fields.Int(dump_only=True)
    name = fields.String(required=True)
    date_of_birth = fields.Date(required=True)
    active = fields.String(required=True,validate=validate.OneOf(('yes','no'))) 
    songs = fields.Nested(lambda: SongsSchema(many=True),dump_only=True,only=('name',),data_key='composed songs')
    periods = fields.Nested(lambda: PeriodsSchema(many=True),dump_only=True,only=('start','end'))
    albums = fields.Nested(lambda: MembersSchema(many=True),dump_only=True,only=('name',),data_key='Discography')

    @post_dump(pass_many=True)
    def member_songs(self,data,many): 
        if many:
            return data
            
        data['composed songs'] = len(data['composed songs'])  
        total_years = 0
        for x in data['periods']:
            try:
                total_years += x['end'] - x['start']
            except TypeError:
                total_years += datetime.now().year - x['start']
        data['active years'] = total_years
        
        return data
     
        
        
    
class SongsSchema(Schema):
    class Meta:
        ordered = True
    
    song_id = fields.Int(dump_only=True)
    number_in_album = fields.Integer(required=True)
    name = fields.String(required=True)
    length = fields.Time(required= True)
    top_popular = fields.String(required=True,validate=validate.OneOf(('yes','no')))
    album = fields.Nested(lambda: AlbumsSchema, dump_only=True, only=('name',) )
    members = fields.Nested(MembersSchema(many=True),dump_only=True,only=('name',),data_key='composer(s)')


    @post_dump(pass_many=True)
    def wrap(self, data, many, **kwargs):
        # if many:
        #     return {'dataxd': data}
        return data  

class AlbumsSchema(Schema):
    class Meta:
        ordered = True 

    album_id = fields.Integer(dump_only=True)
    name = fields.String(required=True)
    release_date = fields.Date(required=True)
    length=fields.Time(required=True)
    cover = fields.Url(required= True)
    album_songs = fields.Nested(SongsSchema(many=True),dump_only=True,only=('name',),data_key='songs') 
    members = fields.Nested(MembersSchema(many=True),dump_only=True,only=('name',),data_key='Personnel')



    @post_dump(pass_many=True)
    def wrap(self, data, many, **kwargs):
        if many:
            return {'Albums': data}
        return data
 
class UsersSchema(Schema):
    class Meta:
        ordered = True

    user_id = fields.Integer(dump_only=True)
    name = fields.String(required=True)
    mail = fields.Email(required=True)
    password = fields.Method(required=True, deserialize='hash_password')
    

    def hash_password(self,password):
        return generate_password_hash(password,'sha256')

class PeriodsSchema(Schema):
    class Meta:
        ordered = True

    period_id = fields.Integer(dump_only=True)
    member_id = fields.Integer(required = True)
    start = fields.Integer(required = True)
    end = fields.Integer(required = True)


class LiveAlbumsSchema(Schema):
    class Meta:
        ordered = True 

    live_album_id = fields.Integer(dump_only=True)
    name = fields.String(required=True)
    release_date = fields.Date(required=True)
    length=fields.Time(required=True)
    #cover = fields.Url(required= True)
    songs = fields.Nested(SongsSchema(many=True),dump_only=True,only=('name',),data_key='songs') 
    #members = fields.Nested(MembersSchema(many=True),dump_only=True,only=('name',),data_key='Personnel')


    @post_dump(pass_many=True)
    def wrap(self, data, many, **kwargs):
        if many:
            return {'Albums': data}
        return data
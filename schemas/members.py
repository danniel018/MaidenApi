from marshmallow import Schema, fields, validate, post_dump
from werkzeug.security import generate_password_hash


class MembersSchema(Schema):
    
    member_id = fields.Int(dump_only=True)
    name = fields.String(required=True)
    date_of_birth = fields.Date(required=True)
    active = fields.String(required=True,validate=validate.OneOf(('yes','no')))  
    
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
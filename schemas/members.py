from marshmallow import Schema, fields, validate, post_dump


class MembersSchema(Schema):
    
    member_id = fields.Int(dump_only=True)
    name = fields.String(required=True)
    date_of_birth = fields.Date(required=True)
    active = fields.String(required=True,validate=validate.OneOf(('yes','no')))  
    
class SongsSchema(Schema):
    
    song_id = fields.Int(dump_only=True)
    number_in_album = fields.Integer(required=True)
    name = fields.String(required=True)
    length = fields.Time(required= True)
    top_popular = fields.String(required=True,validate=validate.OneOf(('yes','no')))

    @post_dump(pass_many=True)
    def wrap(self, data, many, **kwargs):
        if many:
            return {'data': data}
        return data  

class AlbumsSchema(Schema):

    album_id = fields.Integer(dump_only=True)
    name = fields.String(required=True)
    release_date = fields.Date(required=True)
    length=fields.Time(required=True)
    cover = fields.Url(required= True)
    album_songs = fields.Nested(SongsSchema(many=True),dump_only=True,only=('name',)) 
    #members = fields.Nested(MembersSchema,dump_only=True,only=('name',))



    @post_dump(pass_many=True)
    def wrap(self, data, many, **kwargs):
        if many:
            return {'Albums': data}
        return data
 
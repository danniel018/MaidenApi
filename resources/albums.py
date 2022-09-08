from flask import request
from flask_restful import Resource
from http import HTTPStatus
from models.albums import Albums, Songs   
from schemas.members import AlbumsSchema, SongsSchema 

all_albums_schema = AlbumsSchema(many=True,exclude=('cover','length'))
album_schema = AlbumsSchema()
songs_schema = SongsSchema(many=True,only=('name',))
class MaidenAlbums(Resource):

    def get(self):
    
        albums = Albums.all_albums()    
        return all_albums_schema.dump(albums),HTTPStatus.OK

class Album(Resource):

    def get(self,id):
        
        album = Albums.album_by_id(id)
        if album == None:
            return {'data':'not found that'},HTTPStatus.NOT_FOUND 
        
        return album_schema.dump(album),HTTPStatus.OK


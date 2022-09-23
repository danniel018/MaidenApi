from flask import request
from flask_restful import Resource
from http import HTTPStatus
from models.albums import Albums, LiveAlbums   
from schemas.members import AlbumsSchema, SongsSchema , LiveAlbumsSchema
from flask_jwt_extended import jwt_required

all_albums_schema = AlbumsSchema(many=True,exclude=('cover','length'))
album_schema = AlbumsSchema()
songs_schema = SongsSchema(many=True,only=('name',))

all_live_albums_schema = LiveAlbumsSchema(many=True,exclude=('length',))
live_album_schema = LiveAlbumsSchema()
class MaidenAlbums(Resource):

    @jwt_required()
    def get(self):
    
        albums = Albums.all_albums()    
        return all_albums_schema.dump(albums),HTTPStatus.OK

class Album(Resource):

    def get(self,id):
        
        album = Albums.album_by_id(id)
        if album == None:
            return {'data':'not found that'},HTTPStatus.NOT_FOUND 
        
        return album_schema.dump(album),HTTPStatus.OK


class LiveMaidenAlbums(Resource):

    #@jwt_required()
    def get(self):
    
        albums = LiveAlbums.all_albums()    
        return all_live_albums_schema.dump(albums),HTTPStatus.OK

class LiveAlbum(Resource):

    def get(self,id):
        
        album = Albums.album_by_id(id)
        if album == None:
            return {'data':'not found that'},HTTPStatus.NOT_FOUND 
        
        return live_album_schema.dump(album),HTTPStatus.OK

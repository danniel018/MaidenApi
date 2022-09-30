from flask import request
from flask_restful import Resource
from http import HTTPStatus
from models.albums import Albums, LiveAlbums, Songs
from models.members import Members  
from schemas.members import AlbumsSchema, SongsSchema , LiveAlbumsSchema
from flask_jwt_extended import jwt_required

all_albums_schema = AlbumsSchema(many=True,exclude=('cover','length','album_songs','members'))
album_schema = AlbumsSchema()
songs_schema = SongsSchema(only=('name','album','length'))

all_live_albums_schema = LiveAlbumsSchema(many=True,exclude=('length','songs'))
live_album_schema = LiveAlbumsSchema()

class Band(Resource):

    #@jwt_required()
    def get(self):
    
        song = Songs.general_info(query=1)  
        l_song = {'longest song':songs_schema.dump(song)}
        song = Songs.general_info(query=2)
        s_song = {'shortest song':songs_schema.dump(song)}
        song = Songs.general_info(query=3)
        total_songs={'total recorded song':song[0]}

        return [l_song,s_song,total_songs],HTTPStatus.OK




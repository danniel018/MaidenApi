from flask import request
from flask_restful import Resource
from http import HTTPStatus
from models.albums import Albums, LiveAlbums, Songs
from models.members import Members  
from schemas.members import AlbumsSchema, SongsSchema , LiveAlbumsSchema
from flask_jwt_extended import jwt_required
from json import JSONEncoder
from marshmallow import fields ,utils


all_albums_schema = AlbumsSchema(many=True,exclude=('cover','length','album_songs','members'))
album_schema = AlbumsSchema(only=('name','release_date','length'))
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
        avg_song = {'average song length':utils.to_iso_time(song)} 

        song = Songs.general_info(query=4)
        total_songs={'total recorded song':song[0]}

        song = Songs.general_info(query=5)
        most_live={'most recorded live song':{'song':song[0],'times recorded':song[1]}}

        album = Albums.general_info(query=4)
        most={'most songs in an album':{'album':album[0],'songs':album[1]}}

        album = Albums.general_info(query=3)
        avg_album = {'average album length':utils.to_iso_time(album)}

        albums = Albums.general_info(query=5)
        by_decade = {'albums by decade':albums}

        album = Albums.general_info(query=1)  
        l_album = {'longest album':album_schema.dump(album)}
        album = Albums.general_info(query=2)
        s_album = {'shortest album':album_schema.dump(album)}
       
        return [l_song,s_song,total_songs,most_live,avg_song,most,
            avg_album,by_decade,l_album,s_album],HTTPStatus.OK




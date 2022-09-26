from flask import request
from flask_restful import Resource
from http import HTTPStatus
from models.albums import  Songs
from webargs import fields
from webargs.flaskparser import use_kwargs
from schemas.members import SongsSchema

all_songs_schema = SongsSchema(many=True,exclude=('number_in_album','top_popular','live_album','tour'))
song_schema = SongsSchema(exclude=('song_id','top_popular'))

class MaidenSongs(Resource):
    @use_kwargs({'year': fields.Str(missing=None),'composer':fields.Int(missing=None)},location='query')
    def get(self,year,composer):
        
        songs = Songs.all_songs(year=year,composer=composer)      
        return all_songs_schema.dump(songs),HTTPStatus.OK


class PopularSongs(Resource):
    def get(self):
        
        songs = Songs.all_songs(popular=True)          
        return all_songs_schema.dump(songs),HTTPStatus.OK

class Song(Resource):
    def get(self,id):
        main=[]
        data={}
        song = Songs.song_by_id(id)
        if song == None:
            return {'data':'not found that'},HTTPStatus.NOT_FOUND 

        return song_schema.dump(song),HTTPStatus.OK       
from flask import request
from flask_restful import Resource
from http import HTTPStatus
from models.albums import  Songs
from webargs import fields
from webargs.flaskparser import use_kwargs


class MaidenSongs(Resource):
    @use_kwargs({'year': fields.Str(missing=None)},location='query')
    def get(self,year):
        
        songs = Songs.all_songs(year=year)
        data = MaidenSongs.set_data(songs)
      
        return data,HTTPStatus.OK

    @staticmethod
    def set_data(maindata):
        main=[]
        for x in maindata:
            data={}
            data[x.name]={'id':x.song_id,
                'length':str(x.length),'album':x.album.name}
            data[x.name]['composer(s)'] = [i.name for i in x.members]
            main.append(data)
        return main

class PopularSongs(Resource):
    def get(self):
        
        songs = Songs.all_songs(popular=True)
        
        data = MaidenSongs.set_data(songs)
          
        return data,HTTPStatus.OK

class Song(Resource):
    def get(self,id):
        main=[]
        data={}
        song = Songs.song_by_id(id)
        if song == None:
            return {'data':'not found that'},HTTPStatus.NOT_FOUND 

        data['name']=song.name 
        data['length'] = str(song.length) 
        data['album'] = song.album.name 
        data['# in album'] = song.number_in_album
        data['composer(s)'] = [i.name for i in song.members]
        
        main.append(data)

        return main,HTTPStatus.OK       
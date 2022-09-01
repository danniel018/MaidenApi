from flask import request
from flask_restful import Resource
from http import HTTPStatus
from models.albums import Albums, Songs    

class MaidenAlbums(Resource):

    def get(self):
        main=[]
        members = Albums.all_albums()
        
        for x in members:
            data={}
            data[x.name]={'id':x.album_id,'release date':str(x.release_date)}
            songs = Songs.songs_by_id(x.album_id)
            data[x.name]['songs'] = [x.name for x in songs]
            data[x.name]['personnel'] = [i.name for i in x.members]
            #print(x.members.name)
            main.append(data)
          
        return main,HTTPStatus.OK

class Album(Resource):

    def get(self):

        pass
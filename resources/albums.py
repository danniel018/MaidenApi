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
            songs = Songs.songs_by_album(x.album_id)
            data[x.name]['songs'] = [x.name for x in songs]
            data[x.name]['personnel'] = [i.name for i in x.members]
            print(x.release_date.year)
            main.append(data)
          
        return main,HTTPStatus.OK

class Album(Resource):

    def get(self,id):
        
        main=[]
        data={}
        album = Albums.album_by_id(id)
        if album == None:
            return {'data':'not found that'},HTTPStatus.NOT_FOUND 

        data['name']=album.name
        data['release date'] = str(album.release_date)
        data['album cover'] = album.cover
        data['length'] = str(album.length)
        data['personnel'] = [i.name for i in album.members]
        songs = Songs.songs_by_album(id)
        data['songs'] = [x.name for x in songs]
        main.append(data)

        return main,HTTPStatus.OK


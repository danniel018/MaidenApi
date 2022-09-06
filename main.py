from flask import Flask
from flask_restful import  Api
from config import Config
from extensions import db
from resources.members import MaidenMembers, Member
from resources.albums import MaidenAlbums, Album
from resources.songs import MaidenSongs, PopularSongs, Song

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
api = Api(app) 

        
api.add_resource(MaidenMembers,'/members')
api.add_resource(Member,'/members/<int:id>')
api.add_resource(MaidenAlbums,'/albums')
api.add_resource(Album,'/albums/<int:id>')
api.add_resource(MaidenSongs,'/songs')
api.add_resource(PopularSongs,'/songs/popular')
api.add_resource(Song,'/songs/<int:id>')

if __name__ == "__main__":
    app.run(debug=True)


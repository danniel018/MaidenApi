from flask import Flask
from flask_restful import  Api
import os
from config import Config, Production, Development
from extensions import db, jwt
from resources.members import MaidenMembers, Member
from resources.albums import MaidenAlbums, Album, LiveMaidenAlbums, LiveAlbum
from resources.songs import MaidenSongs, PopularSongs, Song
from resources.users import NewUser
from resources.token import Token, RefreshToken,RevokeToken,block_list
from resources.tours import MaidenTours, Tour
from resources.band import Band

env = os.environ.get('ENV', 'Development')
if env == 'Production':
    config = Production()
else:
    config = Development()
    

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)
jwt.init_app(app) 
api = Api(app) 


@jwt.token_in_blocklist_loader
def check_if_token_revoked(jwt_header,jwt_payload): 
    
    jti = jwt_payload['jti']
    return jti in block_list

api.add_resource(MaidenMembers,'/members')
api.add_resource(Member,'/members/<int:id>')

api.add_resource(MaidenAlbums,'/albums') 
api.add_resource(Album,'/albums/<int:id>')
api.add_resource(LiveMaidenAlbums,'/live-albums') 
api.add_resource(LiveAlbum,'/live-albums/<int:id>')

api.add_resource(MaidenSongs,'/songs')
api.add_resource(PopularSongs,'/songs/popular')
api.add_resource(Song,'/songs/<int:id>')

api.add_resource(MaidenTours,'/tours')
api.add_resource(Tour,'/tours/<int:id>')

api.add_resource(NewUser,'/users')

api.add_resource(Band,'/band')


api.add_resource(Token,'/token')
api.add_resource(RefreshToken,'/refresh')
api.add_resource(RevokeToken,'/revoke') 

if __name__ == "__main__":
    app.run()


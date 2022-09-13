from flask import Flask
from flask_restful import  Api
from config import Config
from extensions import db, jwt
from resources.members import MaidenMembers, Member
from resources.albums import MaidenAlbums, Album
from resources.songs import MaidenSongs, PopularSongs, Song
from resources.users import NewUser
from resources.token import Token, RefreshToken,RevokeToken,block_list

app = Flask(__name__)
app.config.from_object(Config)
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
api.add_resource(MaidenSongs,'/songs')
api.add_resource(PopularSongs,'/songs/popular')
api.add_resource(Song,'/songs/<int:id>')
api.add_resource(NewUser,'/users')
api.add_resource(Token,'/token')
api.add_resource(RefreshToken,'/refresh')
api.add_resource(RevokeToken,'/revoke') 

if __name__ == "__main__":
    app.run(debug=True)


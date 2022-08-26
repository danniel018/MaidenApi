from flask import Flask, jsonify, request, make_response
from flask_restful import  Api
from http import HTTPStatus
from config import Config
from extensions import db
from resources.ironmaiden import MaidenMembers

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
api = Api(app) 

        
api.add_resource(MaidenMembers,'/members')
#api.add_resource(Members,'/members/<int:id>')


if __name__ == "__main__":
    app.run(debug=True)


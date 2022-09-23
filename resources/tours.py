from flask import request
from flask_restful import Resource
from http import HTTPStatus
from models.albums import Tours   
from schemas.members import ToursSchema
from flask_jwt_extended import jwt_required



tours_schema = ToursSchema(many=True,exclude=('live_album',))
tour_schema = ToursSchema()

class MaidenTours(Resource):

    #@jwt_required()
    def get(self):
    
        tours = Tours.all_tours()    
        return tours_schema.dump(tours),HTTPStatus.OK

class Tour(Resource):

    def get(self,id):
        
        tour = Tours.tour_by_id(id)
        if tour == None:
            return {'data':'not found that'},HTTPStatus.NOT_FOUND 
        
        return tour_schema.dump(tour),HTTPStatus.OK 
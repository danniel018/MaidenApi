from flask import Flask, jsonify, request, make_response
from flask_restful import Resource, Api
from http import HTTPStatus
app = Flask(__name__)

members = [
    { 'id' : 1,'name':'Steve Harris'},{'id' : 2,'name':'Dave Murray' },{'id' : 3,'name':'Adrian Smith' },
    { 'id' : 4,'name':'Bruce Dickinson'},{'id' : 5,'name':'Nicko McBrain' },{'id' : 6,'name':'Janick Gers' }
]

@app.route('/members',methods=['GET'])
def all_members():
    return jsonify({'data':members},200)

@app.route('/members/<int:id>',methods=['GET'])
def get_member(id):

    for x in members:
        if id == x['id']:
            member = x
            return jsonify (member),HTTPStatus.OK
       
    
    response = make_response (jsonify({'data':'not found that'})),HTTPStatus.NOT_FOUND 
    return response 

if __name__ == "__main__":
    app.run(debug=True)
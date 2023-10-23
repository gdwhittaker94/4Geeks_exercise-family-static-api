"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson") # we send surname to class

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

# GET ALL MEMBERS
@app.route('/members', methods=['GET'])
def get_family():
    # 'jackson_family' variable gives us access to datastructure.py + its methods
    members = jackson_family.get_all_members() # Similar to User.query.filter_by().all
    response_body = members
    return jsonify(response_body), 200

# GET 1 MEMBERS
@app.route('/member/<int:member_id>', methods=['GET'])
def get_member(member_id):
    member = jackson_family.get_member(member_id)
    response_body = member
    return jsonify(response_body), 200

# CREATE NEW FAMILY MEMBER 
@app.route('/member', methods=['POST'])
def add_member():
    body = request.get_json(silent=True)
    if body is None: 
        return jsonify({'msg': 'You must add a body'}), 400
    if 'first_name' not in body: 
        return jsonify({'msg': 'You must add a first name'}), 400
    if 'last_name' not in body: 
        return jsonify({'msg': 'You must add a last name'}), 400
    if 'age' not in body: 
        return jsonify({'msg': 'You must add an age'}), 400
    if 'lucky_numbers' not in body: 
        return jsonify({'msg': "You must add this person's lucky numbers"}), 400
   
    id_number = jackson_family._generateId()
    if id_number in body:
        id_number = body['id_number']

    new_member = {
        'id': id_number,
        'first_name': body['first_name'],
        'last_name': jackson_family.last_name,
        'age': body['age'],
        'lucky_numbers': body['lucky_numbers']
    }
   
    jackson_family.add_member(new_member)
    return jsonify({'msg': 'New family member added', 'new_member': new_member}), 200

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)

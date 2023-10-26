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

# GET 1 MEMBER
@app.route('/member/<int:id>', methods=['GET'])
def get_oneMember(id):
    member = jackson_family.get_member(id)
    if member is None:
        return jsonify({'requested_member_id': member,
                        'msg': 'That family member does not exist'}), 400
    response_body = member
    return jsonify(response_body), 200

# CREATE NEW FAMILY MEMBER 
@app.route('/member', methods=['POST'])
def add_member():
    body = request.get_json(silent=True)
    if body is None: 
        return jsonify({"msg": "You must add a body"}), 400
    if 'first_name' not in body: 
        return jsonify({"msg": "You must specify a 'first_name'"}), 400
    if 'age' not in body: 
        return jsonify({"msg": "You must specify an 'age'"}), 400
    if 'lucky_numbers' not in body: 
        return jsonify({"msg": "You must specify this persons 'lucky_numbers' (in a list format e.g. [1, 2, 3])"}), 400
   
    if id_number in body:
        id_number = body['id_number']
    else: 
        id_number = jackson_family._generateId()

    new_member = {
        'id': id_number,
        'first_name': body['first_name'],
        'last_name': jackson_family.last_name,
        'age': body['age'],
        'lucky_numbers': body['lucky_numbers']
    }

    jackson_family.add_member(new_member)
    family = jackson_family.get_all_members()
    return jsonify({'msg': 'New family member added',
                    'new_member': new_member,
                    'Total family': family}), 200

# DELETE 1 FAMILY MEMBER
@app.route('/member/<int:id>', methods=['DELETE'])
def delete_oneMember(id):
    member = jackson_family.get_member(id)
    if member is None:
        return jsonify({'msg': 'That family member does not exist'}), 400
    jackson_family.delete_member(id)
    deleted_member = member
    current_family = jackson_family.get_all_members()
    return jsonify({
        'done': True,
        'Member removed': deleted_member,
        'Total Family': current_family}), 200

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)

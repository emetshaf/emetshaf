from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flasgger import swag_from
from models import storage, CNC


@app_views.route('/authors', methods=['GET'])
def all_authors():
    """ Retrieves the list of all authors """
    all_authors = storage.all('Author')
    all_authors = list(obj.to_json() for obj in all_authors.values())
    return jsonify(all_authors)


@app_views.route('/authors', methods=['POST'])
def post_Author():
    """ Creates an Author """
    req_data = request.get_json()
    if req_data is None:
        abort(400, 'Not a JSON')
    if req_data.get('name') is None:
        abort(400, 'Missing name')
    Author = CNC['Author']
    new_obj = Author(**req_data)
    new_obj.save()
    return jsonify(new_obj.to_json()), 201


@app_views.route('/authors/<author_id>', methods=['GET'])
def get_author(author_id):
    """ Retrieves a author object """
    author_obj = storage.get('Author', author_id)
    if author_obj is None:
        abort(404, 'Not found')
    return jsonify(author_obj.to_json())


@app_views.route('/authors/<author_id>', methods=['DELETE'])
def delete_author(author_id):
    """ Retrieves a author object """
    author_obj = storage.get('Author', author_id)
    if author_obj is None:
        abort(404, 'Not found')
    del author_obj
    return jsonify({})


@app_views.route('/authors/<author_id>', methods=['PUT'])
def put_author(author_id):
    """ Retrieves a author object """
    author_obj = storage.get('Author', author_id)
    if author_obj is None:
        abort(404, 'Not found')
    req_data = request.get_json()
    if req_data is None:
        abort(400, 'Not a JSON')
    author_obj.bm_update(req_data)
    return jsonify(author_obj.to_json())

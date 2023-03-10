from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flasgger import swag_from
from models import storage, CNC


@app_views.route('/authors', methods=['GET'], strict_slashes=False)
def all_authors():
    """ Retrieves the list of all authors """
    all_authors = storage.all('Author')
    all_authors = list(obj.to_json() for obj in all_authors.values())
    return jsonify(all_authors)


@app_views.route('/authors', methods=['POST'], strict_slashes=False)
def post_Author():
    """ Creates an Author """
    req_data = request.get_json()
    if req_data is None:
        abort(400, 'Not a JSON')
    if req_data.get('first_name') is None:
        abort(400, 'Missing first name')
    if req_data.get('last_name') is None:
        abort(400, 'Missing last name')
    Author = CNC['Author']
    new_obj = Author(**req_data)
    new_obj.save()
    return jsonify(new_obj.to_json()), 201


@app_views.route('/authors/<author_id>', methods=['GET'], strict_slashes=False)
def get_author(author_id):
    """ Retrieves a author object """
    author_obj = storage.get('Author', author_id)
    if author_obj is None:
        abort(404, 'Not found')
    return jsonify(author_obj.to_json())


@app_views.route('/authors/<author_id>/books', methods=['GET'], strict_slashes=False)
def get_books(author_id):
    """ Retrieves a author object """
    return {}


@app_views.route('/authors/<author_id>', methods=['DELETE'], strict_slashes=False)
def delete_author(author_id):
    """ Retrieves a author object """
    author_obj = storage.get('Author', author_id)
    if author_obj is None:
        abort(404, 'Not found')
    author_obj.delete()
    return jsonify({}), 200


@app_views.route('/authors/<author_id>', methods=['PUT'], strict_slashes=False)
def put_author(author_id):
    """ Retrieves a author object """
    author_obj = storage.get('Author', author_id)
    if author_obj is None:
        abort(404, 'Not found')
    req_data = request.get_json()
    if req_data is None:
        abort(400, 'Not a JSON')
    author_obj.bm_update(req_data)
    return jsonify(author_obj.to_json()), 200

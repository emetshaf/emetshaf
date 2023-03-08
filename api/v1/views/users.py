"""
    Flask route that returns json response
"""
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from models import storage, CNC, User
from flasgger.utils import swag_from


def check():
    auth_header = request.headers.get('Authorization')
    if auth_header:
        try:
            auth_token = auth_header.split(" ")[1]
        except IndexError:
            abort(400, 'Invalid token. Please register or login.')
    else:
        abort(400, 'Invalid token. Please register or login.')
    resp = User.decode_auth_token(auth_token)
    if 'Please log in again.' in resp:
        abort(400, resp)


@app_views.route('/users/<user_id>/books/<book_id>', methods=['POST'], strict_slashes=False)
def add_book(user_id, book_id):
    user_obj = storage.get('User', user_id)
    book_obj = storage.get('Book', book_id)
    if user_obj is None:
        abort(404, 'Not found')
    if book_obj is None:
        abort(404, 'Not found')
    user_obj.libraries.append(book_obj)
    user_obj.save()
    return jsonify(user_obj.to_json()), 201


@app_views.route('/users', methods=['GET'], strict_slashes=False)
@swag_from('documentation/users/all_users.yml', methods=['GET'])
def all_users():
    # check()
    all_users = storage.all('User')
    all_users = [obj.to_json() for obj in all_users.values()]
    return jsonify(all_users)


@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
@swag_from('documentation/users/get_user.yml', methods=['GET'])
def post_user(user_id):
    # check()
    user_obj = storage.get('User', user_id)
    if user_obj is None:
        abort(404, 'Not found')
    return jsonify(user_obj.to_json())


@app_views.route('/users/<user_id>/libraries', methods=['GET'], strict_slashes=False)
def get_user_libraries(user_id):
    user_obj = storage.get('User', user_id)
    if user_obj is None:
        abort(404, 'Not found')
    return jsonify(user_obj.to_json())


@app_views.route('/users/<user_id>/favorites', methods=['GET'], strict_slashes=False)
def get_user_favorites(user_id):
    user_obj = storage.get('User', user_id)
    if user_obj is None:
        abort(404, 'Not found')
    return jsonify(user_obj.to_json())


@app_views.route('/users/libraries/', methods=['GET'], strict_slashes=False)
def get_libraries(auth_token):
    resp = User.decode_auth_token(auth_token)
    user_id = resp.get('data').get('id')
    user_obj = storage.get('User', user_id)
    if user_obj is None:
        abort(404, 'Not found')
    return jsonify(user_obj.to_json())


@app_views.route('/users/favorites/', methods=['GET'], strict_slashes=False)
def get_favorites(auth_token):
    resp = User.decode_auth_token(auth_token)
    user_id = resp.get('data').get('id')
    user_obj = storage.get('User', user_id)
    if user_obj is None:
        abort(404, 'Not found')
    return jsonify(user_obj.to_json())


@app_views.route('/users/', methods=['POST'], strict_slashes=False)
@swag_from('documentation/users/post_user.yml', methods=['POST'])
def get_user():
    # check()
    req_data = request.get_json()
    if req_data is None:
        abort(400, 'Not a JSON')
    if req_data.get('username') is None:
        abort(400, 'Missing username')
    if req_data.get('password') is None:
        abort(400, 'Missing password')
    User = CNC.get('User')
    new_object = User(**req_data)
    new_object.save()
    return jsonify(new_object.to_json()), 201


@app_views.route('/users/<user_id>', methods=['DELETE'], strict_slashes=False)
@swag_from('documentation/users/delete_user.yml', methods=['DELETE'])
def delete_user(user_id):
    # check()
    user_obj = storage.get('User', user_id)
    if user_obj is None:
        abort(404, 'Not found')
    user_obj.delete()
    return jsonify({}), 200


@app_views.route('/users/<user_id>', methods=['PUT'], strict_slashes=False)
@swag_from('documentation/users/put_user.yml', methods=['PUT'])
def put_user(user_id):
    user_obj = storage.get('User', user_id)
    if user_obj is None:
        abort(404, 'Not found')
    req_data = request.get_json()
    if req_data is None:
        abort(400, 'Not a JSON')
    user_obj.bm_update(req_data)
    return jsonify(user_obj.to_json()), 200

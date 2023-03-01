from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flasgger import swag_from
from models import storage, CNC


@app_views.route('/narrators', methods=['GET'], strict_slashes=False)
def all_narrators():
    """Get all narrators"""
    all_narrators = storage.all('Narrator')
    all_narrators = list(obj.to_json() for obj in all_narrators.values())
    return jsonify(all_narrators)


@app_views.route('/narrators/<narrator_id>', methods=['GET'], strict_slashes=False)
def get_narrator(narrator_id):
    """Get a narrator by id"""
    narrator = storage.get('Narrator', narrator_id)
    if narrator is None:
        abort(404)
    return jsonify(narrator.to_json())


@app_views.route('/narrators', methods=['POST'], strict_slashes=False)
def create_narrator():
    """Create a narrator"""
    if not request.get_json():
        abort(400, 'Not a JSON')
    data = request.get_json()
    if 'first_name' not in data:
        abort(400, 'Missing First Name')
    if 'last_name' not in data:
        abort(400, 'Missing Last Name')
    narrator = CNC['Narrator'](**data)
    narrator.save()
    return make_response(jsonify(narrator.to_json()), 201)


@app_views.route('/narrators/<narrator_id>', methods=['DELETE'], strict_slashes=False)
def delete_narrator(narrator_id):
    """ Retrieves a narrator object """
    narrator_obj = storage.get('Narrator', narrator_id)
    if narrator_obj is None:
        abort(404, 'Not found')
    narrator_obj.delete()
    return jsonify({}), 200

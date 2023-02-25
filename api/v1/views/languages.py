from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flasgger import swag_from
from models import storage, CNC


@app_views.route('/languages', methods=['GET'])
def all_languages():
    """ Retrieves the list of all languages """
    all_languages = storage.all('Language')
    all_languages = list(obj.to_json() for obj in all_languages.values())
    return jsonify(all_languages)


@app_views.route('/languages', methods=['POST'])
def post_language():
    """ Creates a language """
    req_data = request.get_json()
    if req_data is None:
        abort(400, 'Not a JSON')
    if req_data.get('name') is None:
        abort(400, 'Missing name')
    Language = CNC['Language']
    new_obj = Language(**req_data)
    new_obj.save()
    return jsonify(new_obj.to_json()), 201


@app_views.route('/languages/<language_id>', methods=['GET'])
def get_language(language_id):
    """ Retrieves a language object """
    language_obj = storage.get('Language', language_id)
    if language_obj is None:
        abort(404, 'Not found')
    return jsonify(language_obj.to_json())


@app_views.route('/languages/<language_id>', methods=['DELETE'])
def delete_language(language_id):
    """ Retrieves a language object """
    language_obj = storage.get('Language', language_id)
    if language_obj is None:
        abort(404, 'Not found')
    language_obj.delete()
    return jsonify({}), 200


@app_views.route('/languages/<language_id>', methods=['PUT'])
def put_language(language_id):
    """ Retrieves a language object """
    language_obj = storage.get('Language', language_id)
    if language_obj is None:
        abort(404, 'Not found')
    req_data = request.get_json()
    if req_data is None:
        abort(400, 'Not a JSON')
    language_obj.bm_update(req_data)
    return jsonify(language_obj.to_json())

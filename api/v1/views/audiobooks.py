from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flasgger import swag_from
from models import storage, CNC


@app_views.route('/audiobooks', methods=['GET'], strict_slashes=False)
def all_audiobooks():
    """ Retrieves the list of all audiobooks """
    all_audiobooks = storage.all('AudioBook')
    all_audiobooks = list(obj.to_json() for obj in all_audiobooks.values())
    return jsonify(all_audiobooks)


@app_views.route('/audiobooks', methods=['POST'], strict_slashes=False)
def post_AudioBook():
    """ Creates an Author """
    req_data = request.get_json()
    if req_data is None:
        abort(400, 'Not a JSON')
    if req_data.get('file') is None:
        abort(400, 'Missing file')
    AudioBook = CNC['AudioBook']
    new_obj = AudioBook(**req_data)
    new_obj.save()
    return jsonify(new_obj.to_json()), 201


@app_views.route('/audiobooks/<audiobook_id>', methods=['DELETE'], strict_slashes=False)
def delete_audiobook(audiobook_id):
    """ Retrieves a audiobook object """
    audiobook_obj = storage.get('AudioBook', audiobook_id)
    if audiobook_obj is None:
        abort(404, 'Not found')
    audiobook_obj.delete()
    return jsonify({}), 200

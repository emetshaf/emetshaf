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

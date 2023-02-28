from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flasgger import swag_from
from models import storage, CNC


@app_views.route('/reviews', methods=['GET'], strict_slashes=False)
def all_reviews():
    """ Retrieves the list of all reviews """
    all_reviews = storage.all('Review')
    all_reviews = list(obj.to_json() for obj in all_reviews.values())
    return jsonify(all_reviews)

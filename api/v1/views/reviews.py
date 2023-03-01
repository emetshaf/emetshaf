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


@app_views.route('/reviews', methods=['POST'], strict_slashes=False)
def post_review():
    """ Creates a review """
    req_data = request.get_json()
    if req_data is None:
        abort(400, 'Not a JSON')
    if req_data.get('text') is None:
        abort(400, 'Missing text')
    Review = CNC['Review']
    new_obj = Review(**req_data)
    new_obj.save()
    return jsonify(new_obj.to_json()), 201


@app_views.route('/reviews/<review_id>', methods=['GET'], strict_slashes=False)
def get_review(review_id):
    """ Retrieves a review object """
    review_obj = storage.get('Review', review_id)
    if review_obj is None:
        abort(404, 'Not found')
    return jsonify(review_obj.to_json())


@app_views.route('/reviews/<review_id>', methods=['DELETE'], strict_slashes=False)
def delete_review(review_id):
    """ Retrieves a review object """
    review_obj = storage.get('Review', review_id)
    if review_obj is None:
        abort(404, 'Not found')
    review_obj.delete()
    return jsonify({}), 200


@app_views.route('/reviews/<review_id>', methods=['PUT'], strict_slashes=False)
def put_review(review_id):
    """ Retrieves a review object """
    review_obj = storage.get('Review', review_id)
    if review_obj is None:
        abort(404, 'Not found')
    req_data = request.get_json()
    if req_data is None:
        abort(400, 'Not a JSON')
    review_obj.bm_update(req_data)
    return jsonify(review_obj.to_json())

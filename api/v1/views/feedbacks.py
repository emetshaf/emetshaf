from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flasgger import swag_from
from models import storage, CNC


@app_views.route('/feedbacks', methods=['GET'], strict_slashes=False)
def get_feedbacks():
    """
    Retrieves the list of all Feedback objects
    """
    all_feedbacks = storage.all('Feedback')
    all_feedbacks = list(obj.to_json() for obj in all_feedbacks.values())
    return jsonify(all_feedbacks)


@app_views.route('/feedbacks/<feedback_id>', methods=['GET'], strict_slashes=False)
def get_feedback(feedback_id):
    """
    Retrieves a Feedback object
    """
    feedback = storage.get('Feedback', feedback_id)
    if feedback is None:
        abort(404)
    return jsonify(feedback.to_json())


@app_views.route('/feedbacks', methods=['POST'], strict_slashes=False)
def create_feedback():
    """
    Creates a Feedback
    """
    feedback = request.get_json()
    if feedback is None:
        abort(400, 'Not a JSON')
    if 'full_name' not in feedback:
        abort(400, 'Missing full_name')
    if 'email' not in feedback:
        abort(400, 'Missing email')
    if 'message' not in feedback:
        abort(400, 'Missing message')
    new_feedback = CNC['Feedback'](**feedback)
    new_feedback.save()
    return make_response(jsonify(new_feedback.to_json()), 201)


@app_views.route('/feedbacks/<feedback_id>', methods=['DELETE'], strict_slashes=False)
def delete_feedback(feedback_id):
    """ Retrieves a feedback object """
    feedback_obj = storage.get('Feedback', feedback_id)
    if feedback_obj is None:
        abort(404, 'Not found')
    feedback_obj.delete()
    return jsonify({}), 200


@app_views.route('/feedbacks/<feedback_id>', methods=['PUT'], strict_slashes=False)
def put_feedback(feedback_id):
    """ Retrieves a feedback object """
    feedback_obj = storage.get('Feedback', feedback_id)
    if feedback_obj is None:
        abort(404, 'Not found')
    req_data = request.get_json()
    if req_data is None:
        abort(400, 'Not a JSON')
    feedback_obj.bm_update(req_data)
    return jsonify(feedback_obj.to_json()), 200

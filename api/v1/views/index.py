"""
Flask route that returns json status response
"""
from api.v1.views import app_views
from flask import jsonify, request
from models import storage
from flasgger.utils import swag_from


@app_views.route('/status', methods=['GET'], strict_slashes=False)
@swag_from('documentation/health/status.yml')
def status():
    """
    function for status route that returns the status
    """
    resp = {"status": "OK"}
    return jsonify(resp)


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def stats():
    """
    function to return the count of all class objects
    """
    response = {}
    PLURALS = {
        "AudioBook": "audiobooks",
        "Author": "authors",
        "Book": "books",
        "Category": "categories",
        "Feedback": "feedbacks",
        "Language": "languages",
        "Narrator": "narrators",
        "SubCategory": "subcategories",
        "Review": "reviews",
        "User": "users"
    }
    for key, value in PLURALS.items():
        response[value] = storage.count(key)
    return jsonify(response)

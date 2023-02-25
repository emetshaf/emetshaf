from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flasgger import swag_from
from models import storage, CNC


@app_views.route('/categories', methods=['GET'], strict_slashes=False)
def all_categories():
    """ Retrieves the list of all categories """
    all_categories = storage.all('Category')
    all_categories = list(obj.to_json() for obj in all_categories.values())
    return jsonify(all_categories)


@app_views.route('/categories', methods=['POST'], strict_slashes=False)
def post_Category():
    """ Creates an Category """
    req_data = request.get_json()
    if req_data is None:
        abort(400, 'Not a JSON')
    if req_data.get('name') is None:
        abort(400, 'Missing name')
    Category = CNC['Category']
    new_obj = Category(**req_data)
    new_obj.save()
    return jsonify(new_obj.to_json()), 201


@app_views.route('/categories/<category_id>', methods=['GET'], strict_slashes=False)
def get_category(category_id):
    """ Retrieves a category object """
    category_obj = storage.get('Category', category_id)
    if category_obj is None:
        abort(404, 'Not found')
    return jsonify(category_obj.to_json())


@app_views.route('/categories/<category_id>', methods=['DELETE'], strict_slashes=False)
def delete_category(category_id):
    """ Retrieves a category object """
    category_obj = storage.get('Category', category_id)
    if category_obj is None:
        abort(404, 'Not found')
    category_obj.delete()
    return jsonify({}), 200


@app_views.route('/categories/<category_id>', methods=['PUT'], strict_slashes=False)
def put_category(category_id):
    """ Retrieves a category object """
    category_obj = storage.get('Category', category_id)
    if category_obj is None:
        abort(404, 'Not found')
    req_data = request.get_json()
    if req_data is None:
        abort(400, 'Not a JSON')
    for key, value in req_data.items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(category_obj, key, value)
    category_obj.save()
    return jsonify(category_obj.to_json()), 200


@app_views.route('/subcategories', methods=['GET'], strict_slashes=False)
def all_subcategories():
    """ Retrieves the list of all subcategories """
    all_subcategories = storage.all('SubCategory')
    all_subcategories = list(obj.to_json()
                             for obj in all_subcategories.values())
    return jsonify(all_subcategories)


@app_views.route('/subcategories', methods=['POST'], strict_slashes=False)
def post_SubCategory():
    """ Creates an SubCategory """
    req_data = request.get_json()
    if req_data is None:
        abort(400, 'Not a JSON')
    if req_data.get('name') is None:
        abort(400, 'Missing name')
    SubCategory = CNC['SubCategory']
    new_obj = SubCategory(**req_data)
    new_obj.save()
    return jsonify(new_obj.to_json()), 201


@app_views.route('/subcategories/<subcategory_id>', methods=['GET'], strict_slashes=False)
def get_subcategory(subcategory_id):
    """ Retrieves a subcategory object """
    subcategory_obj = storage.get('SubCategory', subcategory_id)
    if subcategory_obj is None:
        abort(404, 'Not found')
    return jsonify(subcategory_obj.to_json())


@app_views.route('/subcategories/<subcategory_id>', methods=['DELETE'], strict_slashes=False)
def delete_subcategory(subcategory_id):
    """ Retrieves a subcategory object """
    subcategory_obj = storage.get('SubCategory', subcategory_id)
    if subcategory_obj is None:
        abort(404, 'Not found')
    subcategory_obj.delete()
    return jsonify({}), 200


@app_views.route('/subcategories/<subcategory_id>', methods=['PUT'], strict_slashes=False)
def put_subcategory(subcategory_id):
    """ Retrieves a subcategory object """
    subcategory_obj = storage.get('SubCategory', subcategory_id)
    if subcategory_obj is None:
        abort(404, 'Not found')
    req_data = request.get_json()
    if req_data is None:
        abort(400, 'Not a JSON')
    for key, value in req_data.items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(subcategory_obj, key, value)
    subcategory_obj.save()
    return jsonify(subcategory_obj.to_json()), 200

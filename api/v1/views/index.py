from api.v1.views import app_views
from flask import jsonify, request
from models import storage
from models.user import User


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def number_objects():
    classes = [User]
    names = ['users']

    num_objs = {}
    for i in range(len(classes)):
        num_objs[names[i]] = storage.count(classes[i])

    return jsonify(num_objs)


@app_views.route('/signup', methods=['POST'], strict_slashes=False)
def signup():
    pass


@app_views.route('/signin', methods=['POST'], strict_slashes=False)
def signin():
    _username = request.json['username']
    _password = request.json['password']
    if _username and _password:
        return jsonify({
            'message': 'Success'
        })
    else:
        return jsonify({'message': 'fail'}).status_code(400)


@app_views.route('/signout', methods=['POST'], strict_slashes=False)
def signout():
    pass

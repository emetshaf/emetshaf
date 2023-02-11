from api.v1.views import app_views
from flasgger import Swagger
from flasgger.utils import swag_from
from flask import Flask, jsonify, make_response, session
from flask_cors import CORS
from models import storage
from datetime import timedelta

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.config['SECRET_KEY'] = ''
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=10)
app.register_blueprint(app_views)
cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})


@app.teardown_appcontext
def close_db(error):
    storage.close()


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': "Not found"}), 404)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', threaded=True, debug=True)

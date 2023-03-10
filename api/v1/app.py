"""
Flask App that integrates with AirBnB static HTML Template
"""
from api.v1.views import app_views, auth_blueprint
from dotenv import load_dotenv
from flasgger import Swagger
from flask import (
    Flask, jsonify, make_response, render_template, url_for, request)
from flask_cors import CORS, cross_origin
from models import storage
from werkzeug.exceptions import HTTPException
from os import environ
import logging


load_dotenv()

logging.basicConfig(level=logging.DEBUG, filename='api.log', filemode='w',
                    format='%(name)s - %(levelname)s - %(message)s')


SECRET_KEY = environ.get('SECRET_KEY')
UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

# Global Flask Application Variable: app
app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024
app.config['SWAGGER'] = {'title': 'EMetshaf Restful API', 'uiversion': 3}

swagger_config = Swagger.DEFAULT_CONFIG
swagger_config['swagger_ui_bundle_js'] = (
    '//unpkg.com/swagger-ui-dist@3/swagger-ui-bundle.js')
swagger_config['swagger_ui_standalone_preset_js'] = (
    '//unpkg.com/swagger-ui-dist@3/swagger-ui-standalone-preset.js')
swagger_config['jquery_js'] = (
    '//unpkg.com/jquery@2.2.4/dist/jquery.min.js')
swagger_config['swagger_ui_css'] = (
    '//unpkg.com/swagger-ui-dist@3/swagger-ui.css')
swagger = Swagger(app, config=swagger_config)

# global strict slashes
app.url_map.strict_slashes = False

# Cross-Origin Resource Sharing
# cors = CORS(app)
cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

# app_views BluePrint defined in api.v1.views
app.register_blueprint(app_views)
app.register_blueprint(auth_blueprint)


# begin flask page rendering
@app.teardown_appcontext
def teardown_db(exception):
    """
    after each request, this method calls .close() (i.e. .remove()) on
    the current SQLAlchemy Session
    """
    storage.close()


@app.errorhandler(404)
def handle_404(exception):
    """
    handles 404 errors, in the event that global error handler fails
    """
    code = exception.__str__().split()[0]
    description = exception.description
    message = {'error': description}
    return make_response(jsonify(message), code)


@app.errorhandler(413)
def request_entity_too_large(error):
    return 'File Too Large', 413


@app.errorhandler(400)
def handle_404(exception):
    """
    handles 400 errros, in the event that global error handler fails
    """
    code = exception.__str__().split()[0]
    description = exception.description
    message = {'error': description}
    return make_response(jsonify(message), code)


@app.errorhandler(Exception)
def global_error_handler(err):
    """
        Global Route to handle All Error Status Codes
    """
    if isinstance(err, HTTPException):
        if type(err).__name__ == 'NotFound':
            err.description = "Not found"
        message = {'error': err.description}
        code = err.code
    else:
        message = {'error': err}
        code = 500
    return make_response(jsonify(message), code)


def setup_global_errors():
    """
    This updates HTTPException Class with custom error function
    """
    for cls in HTTPException.__subclasses__():
        app.register_error_handler(cls, global_error_handler)


if __name__ == "__main__":
    """
    MAIN Flask App
    """
    # initializes global error handling
    setup_global_errors()
    # start Flask app
    app.run(host='0.0.0.0', port=5005, threaded=True)

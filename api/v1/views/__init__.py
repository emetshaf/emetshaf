from flask import Blueprint
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
auth_blueprint = Blueprint('auth', __name__, url_prefix='/auth')
from api.v1.views.authentication import *  # noqa
from api.v1.views.index import *  # noqa
from api.v1.views.authors import *
from api.v1.views.books import *
from api.v1.views.categories import *
from api.v1.views.languages import *
from api.v1.views.users import *  # noqa

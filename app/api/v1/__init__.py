from flask import Blueprint
from flask_restful import Api

from .views.app import Home

version_1 = Blueprint('api_v1', __name__, url_prefix='/api/v1')
api = Api(version_1)


api.add_resource(Home, '/')



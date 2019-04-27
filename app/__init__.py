from flask import Flask, Blueprint
from flask import Flask, jsonify, request, make_response
from instance.config import app_config

from .api.v1 import version_1 as v1

def create_app(config_name='development'):
	app = Flask(__name__, instance_relative_config=True)
	app.url_map.strict_slashes = False

	app.config.from_pyfile('config.py')
	app.register_blueprint(v1)
	app.config['SECRET_KEY'] = 'REFUGE'

	return app


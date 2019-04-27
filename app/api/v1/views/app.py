from flask import Flask, jsonify, request, make_response
from flask_restful import Resource
import datetime
import json
import random

class Home(Resource):
	def get(self):
		return {"message" : "Dj Refuge Wise"}


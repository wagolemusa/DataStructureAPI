from flask import Flask, jsonify, request, make_response
from flask_restful import Resource
import datetime
import json
import random
import africastalking


class Home(Resource):
	def get(self):
		return {"message" : "Dj Refuge Wise"}

class Send(Resource):
	def post(self):
		data = request.get_json(force=True)
		
		message = data['message']
		phone  = data['phone']

		print ('+' + phone)
		# print (musa)
		# Initialize SDK
		username = "refuge"    # use 'sandbox' for development in the test environment
		api_key = "73d787253bd6446b12686b20f063042cbfc7d687301f4ab8a89233b6dd523883"      # use your sandbox app API key for development in the test environment
		africastalking.initialize(username, api_key)

		# Initialize a service e.g. SMS
		sms = africastalking.SMS
		# Use the service synchronously
		response = sms.send(message, ['+' + phone])
		print(response)





from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
import sqlalchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URL'] =  'postgresql://postgres:refuge@localhost/origin'
app.config['SECRET_KEY']='refuge'

db = SQLAlchemy(app)

class Person(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(20))
	# it looks a class in python code
	pets = db.relationship('Pet', backref='owner')


class Pet(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(20))
	# it looks the relationship in our database
	owner_id = db.Column(db.Integer, db.ForeignKey('person.id'))



if __name__ =="__main__":
	app.run()
#!/usr/bin/python3

from datetime import datetime
from flask import Flask
from flask_login import UserMixin
from sqlalchemy import Column, Integer, String, MetaData
from views import db
import uuid

"""
The following lines of code are only important when buiding a database mode from flask.
To create the model, carry out the following command  within the file's directory.
-> export FLASK_APP=property
-> flask shell

Withing the flask console:
>>>from models.property import db, Property
>>>db.create_all()
"""
# Create the flask application object
app = Flask(__name__)

# This configuration establishes a connection between the database and the flask app
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://end_user:password@localhost:3306/house_hunter'

# Initialize the SQLAlchemy extension
db.init_app(app)

class Property(db.Model, UserMixin):
    __tablename__ = 'houses'
    id = Column(db.String(60), primary_key=True, nullable=False)
    created_at = Column(db.DateTime, default=datetime.utcnow(), nullable=False)
    updated_at = Column(db.DateTime, default=datetime.utcnow(), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    cost = db.Column(db.Integer(), nullable=False)
    Rooms = db.Column(db.Integer(), nullable=False)
    Location = db.Column(db.String(128), nullable=False)
    estate = db.Column(db.String(128), nullable=False)
    electricity = db.Column(db.String(128), nullable=False)
    water_availability = db.Column(db.String(128), nullable=False)
    internet_provider = db.Column(db.String(128), nullable=False)
    parking = db.Column(db.String(128), nullable=False)
    security = db.Column(db.String(128), nullable=False)
    garbage_collection = db.Column(db.String(128), nullable=False)
    photo = db.Column(db.LargeBinary, nullable=False)

    def __init__(self, email, cost, rooms, location, estate, water_availability, internet_provider, parking, security, garbage_collection, electricity, photo):
        self.id = str(uuid.uuid4())
        self.email = email
        self.cost = cost
        self.rooms = rooms
        self.location = location
        self.estate = estate
        self.water_availability = water_availability
        self.internet_provider = internet_provider
        self.parking = parking
        self.security = security
        self.garbage_collection = garbage_collection
        self.electricity = electricity
        self.photo = photo
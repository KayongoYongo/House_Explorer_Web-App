#!/usr/bin/python3

from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, MetaData
import uuid

# Create the flask application object
app = Flask(__name__)

# This establishes a connection between the database and the flask app
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://end_user:password@localhost:3306/house_hunter'

# Create the db object
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'
    id = Column(db.String(60), primary_key=True, nullable=False)
    created_at = Column(db.DateTime, default=datetime.utcnow(), nullable=False)
    updated_at = Column(db.DateTime, default=datetime.utcnow(), nullable=False)
    name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    password_1 = db.Column(db.String(128), nullable=False)
    password_2 = db.Column(db.String(128), nullable=False)

    def __init__(self, name, email):
        self.id = str(uuid.uuid4())
        self.name = name
        self.email = email

#!/usr/bin/python3

from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.dialects.mysql import CHAR
import uuid

# Create the flask application object
app = Flask(__name__)

# This establishes a connection between the database and the flask app
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://new_user:password@localhost:3306/house_hunter'

# Create the db object
db = SQLAlchemy(app)

class House(db.Model):
    __tablename__ = 'houses'
    id = Column(CHAR(36), default=str(uuid.uuid4()), primary_key=True, unique=True, nullable=False)
    created_at = Column(db.DateTime, default=datetime.utcnow(), nullable=False)
    updated_at = Column(db.DateTime, default=datetime.utcnow(), nullable=False)
    name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)

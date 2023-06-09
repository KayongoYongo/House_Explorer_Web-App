#!/usr/bin/python3

from views import db
from datetime import datetime
from flask_login import UserMixin
from sqlalchemy import Column, Integer, String, MetaData
import uuid

"""
The following lines of code are only important when buiding a database mode from flask.
To create the model, carry out the following command  within the file's directory.
-> export FLASK_APP=users
-> flask shell

Withing the flask console:
>>>from models.users import db, Student
>>>db.create_all()

# Create the flask application object
app = Flask(__name__)

# This configuration establishes a connection between the database and the flask app
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://end_user:password@localhost:3306/house_hunter'

# Initialize the SQLAlchemy extension
db.init_app(app)
"""

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = Column(db.String(60), primary_key=True, nullable=False)
    created_at = Column(db.DateTime, default=datetime.utcnow(), nullable=False)
    updated_at = Column(db.DateTime, default=datetime.utcnow(), nullable=False)
    name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    password_1 = db.Column(db.String(128), nullable=False)
    password_2 = db.Column(db.String(128), nullable=False)

    def __init__(self, name, email, password_1, password_2):
        self.id = str(uuid.uuid4())
        self.name = name
        self.email = email
        self.password_1 = password_1
        self.password_2 = password_2
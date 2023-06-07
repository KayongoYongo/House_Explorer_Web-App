from flask import Blueprint
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Create a universal blueprint
app_views = Blueprint('app_views', __name__, url_prefix='/views')

# Create the flask application object
app = Flask(__name__)

# This establishes a connection between the database and the flask app
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://end_user:password@localhost:3306/house_hunter'

# Create the db object
db = SQLAlchemy(app)

from views.house import *
from views.sign_up import *
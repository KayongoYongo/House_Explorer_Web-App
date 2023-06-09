#!/usr/bin/python3

from flask import Blueprint, render_template, request
from models.property import Property

property_blueprint = Blueprint('house_blueprint', __name__)
"""
# Create the flask application object
# app = Flask(__name__)

# This establishes a connection between the database and the flask app
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://end_user:password@localhost:3306/house_hunter'

# Set the track modifications option to False
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
"""

# Create a route to handle form submission
@property_blueprint.route('/create_house', methods=['POST'])
def create_house():
    """
    # Get form data
    name = request.form.get('name')
    email = request.form.get('email')

    # Create an instance of the model
    form_data = House(name=name, email=email)

    # Add the instance to the session and commit changes
    db.session.add(form_data)
    db.session.commit()

    print('Data submitted successfully')
    """
    return render_template('home.html')
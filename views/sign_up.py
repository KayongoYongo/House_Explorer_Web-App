#!/usr/bin/python3

from flask import abort, Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from models.users import User
from views import app_views
from views import db

# Create the flask application object
app = Flask(__name__)

# This establishes a connection between the database and the flask app
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://end_user:password@localhost:3306/house_hunter'

# Set the track modifications option to False
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Create a route to handle form submission
@app_views.route('/sign_up', methods=['POST'])
def create_user():
    # Get form data and store it in a varaible
    name = request.form.get('name')
    email = request.form.get('email')
    password_1 = request.form.get('password_1')
    password_2 = request.form.get('password_2')

    #Data validation of the form
    #Checks if they are empty
    if not name or not email or not password_1 or not password_2:
        error_statement = "All from fields are required!"
        return render_template("sign_up.html", error_statement=error_statement)

    # Checks if the passwords match  
    if password_1 != password_2:
        error_statement = "The passwords do not match!"
        return render_template("sign_up.html", error_statement=error_statement)
    
    # Checks if the password is long
    if len(password_1) < 6 and len(password_2) < 6:
        error_statement = "The password is too short!"
        return render_template("sign_up.html", error_statement=error_statement)
    
    # Checks if the users email exists
    # if User.query.filter_by(email=email).first() == email:
    #    error_statement = "Email address already exists!"
    #    return render_template("sign_up.html", error_statement=error_statement)
    
    # Create an instance of the model
    form_data = User(name=name, email=email, password_1=password_1, password_2=password_2)

    print(form_data)

    # Add the instance to the session and commit changes
    db.session.add(form_data)
    db.session.commit()

    return render_template("home.html", )
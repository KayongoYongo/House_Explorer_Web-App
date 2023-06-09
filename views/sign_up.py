#!/usr/bin/python3

from flask import Blueprint, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from models.users import User
from views.form_validator import validate_form_data
from views import db


users_blueprint = Blueprint('users_blueprint', __name__)

# Create a route to handle form submission
@users_blueprint.route('/sign-up', methods=['POST'])
def create_user():

    # Get form data and store it in a varaible
    name = request.form.get('name')
    email = request.form.get('email')
    password_1 = request.form.get('password_1')
    password_2 = request.form.get('password_2')

    # Data validation of the form
    # Call the form validator function
    error_statement = validate_form_data(name, email, password_1, password_2)

    if error_statement:
        return render_template("sign_up.html", error_statement=error_statement, user=None)

    # Create an instance of the model
    form_data = User(name=name, email=email, password_1=password_1, password_2=password_2)

    # Add the instance to the session and commit changes
    db.session.add(form_data)
    db.session.commit()

    return redirect(url_for('site_views.log_in'))
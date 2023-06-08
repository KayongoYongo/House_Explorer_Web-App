#!/usr/bin/python3

from flask import Blueprint, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from models.users import User
from views import db


login_blueprint = Blueprint('login_blueprint', __name__)

# Create a route to handle form submission
@login_blueprint.route('/log-in', methods=['POST'])
def login_user():
    # Get form data and store it in a varaible
    email = request.form.get('email')
    password_1 = request.form.get('password_1')

    # Checks the database for a unique user
    user = User.query.filter_by(email=email).first()

    # Define the variable before using it
    error_statement = None  

    if user:
        if (user.password_1, password_1):
            error_statement = "Log In Successful"
            return render_template("home.html", error_statement=error_statement)
        else:
            error_statement = "incorrect password"
    else:
            error_statement = "Email does not exist!"

    if error_statement:
         return render_template("log_in.html", error_statement=error_statement)

    return redirect(url_for('site_views.home_page'))
        
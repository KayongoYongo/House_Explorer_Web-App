#!/usr/bin/python3

from flask import Blueprint, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_user as login_module
from flask_login import login_required, logout_user, current_user
from models.users import User
from views import db

login_blueprint = Blueprint('login_blueprint', __name__)

# Create a route to handle form submission
@login_blueprint.route('/login', methods=['POST'])
def login_user():
    # Get form data and store it in a varaible
    email = request.form.get('email')
    password_1 = request.form.get('password_1')

    # Checks the database for a unique user
    user = User.query.filter_by(email=email).first()

    # Define the variable before using it
    error_statement = None  

    if user:
        if (user.password_1 == password_1):
            error_statement = "Log In Successful"
            # This is going to make sure the user is logged in within the flask session
            login_module(user, remember=True)
            user_id = user.id
            return render_template("home.html", user=current_user, user_id=user_id, error_statement=error_statement)
        else:
            error_statement = "incorrect password"
    else:
        error_statement = "Email does not exist!"

    if error_statement:
         return render_template("log_in.html", error_statement=error_statement, user=current_user)
    
    return redirect(url_for('site_views.home_page'))
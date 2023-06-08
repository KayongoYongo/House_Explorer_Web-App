#!/usr/bin/python3

from models.users import User

def validate_form_data(name, email, password_1, password_2):
    # Data validation of the form
    # Checks if they are empty
    if not name or not email or not password_1 or not password_2:
        error_statement = "All form fields are required!"
        return error_statement

    # Checks if the passwords match  
    elif password_1 != password_2:
        error_statement = "The passwords do not match!"
        return error_statement
    
    # Checks if the password is too short
    elif len(password_1) < 6 and len(password_2) < 6:
        error_statement = "The password is too short!"
        return error_statement
    
    # Check if the user's email exists
    existing_user = User.query.filter_by(email=email).first()

    if email == existing_user:
        error_statement = "The email already exists!"
        return error_statement

    # If all validation passes, return None (no error)
    return None

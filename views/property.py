#!/usr/bin/python3

from flask import Blueprint, render_template, request, redirect, url_for
from models.property import Property
from flask_login import current_user
from models.users import User
from views.file_upload import save_file
from views import db

property_blueprint = Blueprint('property_blueprint', __name__)

# Create a route to handle form submission
@property_blueprint.route('/houses/<user_id>', methods=['POST'])
def create_property(user_id):
    # Store thr form data in variables
    cost = request.form.get('cost')
    rooms = request.form.get('rooms')
    county = request.form.get('county')
    estate = request.form.get('estate')
    water_availability = request.form.get('water_availability')
    internet_provider = request.form.get('internet_provider')
    parking = request.form.get('parking')
    security = request.form.get('security')
    garbage_collection = request.form.get('garbage_collection')
    electricity = request.form.get('electricity')
    photo = request.files['photo']
    file_path = save_file(photo)

    form_data = Property(user_id=user_id, cost=cost, rooms=rooms, county=county, estate=estate, 
                        water_availability=water_availability, internet_provider=internet_provider,
                        parking=parking, security=security, garbage_collection=garbage_collection,
                        electricity=electricity, photo=file_path)

    # Add the instance to the session and commit changes
    db.session.add(form_data)
    db.session.commit()

    print('Data submitted successfully')

    return render_template('home.html', user=current_user)
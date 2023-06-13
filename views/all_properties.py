#!/usr/bin/python3

from flask import Blueprint, render_template, request, redirect, url_for, current_app
from flask import session
from flask_login import current_user
from models.property import Property
from views import db
import os

display_all_blueprint = Blueprint('display_all_blueprint', __name__)

# Custom Jinja2 filter for emulating enumerate behavior
def my_enumerate(iterable, start=0):
    return zip(range(start, start + len(iterable)), iterable)

# Register the custom filter in the Jinja2 environment
display_all_blueprint.add_app_template_filter(my_enumerate, 'enumerate')

@display_all_blueprint.route('/properties/images/', methods=['GET'])
def images():
    image_folder = os.path.join(os.path.dirname(__file__), 'static', 'UPLOADS')
    # The image files are created in a lexicographic order
    image_files = sorted([filename for filename in os.listdir(image_folder) if filename.endswith('.jpg')], key=str.lower)
    # image_files = [filename for filename in os.listdir(image_folder) if filename.endswith('.jpg')]

    # Print create image paths
    image_paths = [os.path.join(image_folder, filename) for filename in image_files]

    # Retrieve the matching columns for cost, rooms, counties, estate, and photo (file paths) 
    matching_properties = Property.query.filter(Property.photo.in_(image_paths)).with_entities(
    Property.cost, Property.rooms, Property.county, Property.estate, Property.photo,
    Property.id, Property.water_availability, Property.electricity, Property.internet_provider,
    Property.parking, Property.security, Property.garbage_collection).all()

    # Matchting properties sorted in lexicographic order
    matching_properties_sorted = sorted(matching_properties, key=lambda x: x[4])

    print(matching_properties)
    print(image_files)

    return render_template('view_properties.html', image_files=image_files, user=current_user, matching_properties=matching_properties_sorted)
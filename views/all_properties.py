#!/usr/bin/python3

from flask import Blueprint, render_template, request, redirect, url_for, current_app
from flask_login import current_user
import os

display_all_blueprint = Blueprint('display_all_blueprint', __name__)

@display_all_blueprint.route('/properties/images/', methods=['GET'])
def images():
    image_folder = os.path.join(os.path.dirname(__file__), 'static', 'UPLOADS')
    image_files = [filename for filename in os.listdir(image_folder) if filename.endswith('.jpg')]
    print(image_files)
    return render_template('view_properties.html', image_files=image_files, user=current_user)
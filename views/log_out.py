#!/usr/bin/python3

from flask import Blueprint, render_template
from flask_login import login_required, logout_user, current_user

logout_blueprint = Blueprint('logout_blueprint', __name__)

@logout_blueprint.route('/home')
@login_required
def log_out():
     logout_user()
     return render_template('home.html', user=None)
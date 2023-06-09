from flask import Blueprint, render_template
from flask_login import login_required, current_user

# Create a blueprint to handle different routes within the web page
site_views = Blueprint('site_views', __name__, static_folder='static', template_folder='templates', static_url_path='/static')

@site_views.route('/')
@site_views.route('/home')
def home_page():
    return render_template('home.html', user=None)

@site_views.route('/houses')
@login_required
def house_page():
    return render_template('House.html', user=current_user)

@site_views.route('/about')
def about_page():
    return render_template('about.html', user=None)

@site_views.route('/sign_up')
def sign_page():
    return render_template('sign_up.html', user=None)

@site_views.route('/log_in')
def log_in():
    return render_template('log_in.html', user=None)
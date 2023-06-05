from flask import Blueprint, Flask
from flask import render_template

# Create a blueprint to handle different routes within the web page
site_views = Blueprint('site_views', __name__, static_folder='static', template_folder='templates', static_url_path='/static')

# app = Flask(__name__, static_folder='static', static_url_path='/static')

@site_views.route('/')
@site_views.route('/home')
def home_page():
    return render_template('home.html')

@site_views.route('/houses')
def house_page():
    return render_template('House.html')

@site_views.route('/about')
def about_page():
    return render_template('About.html')

@site_views.route('/sign_up')
def sign_page():
    return render_template('sign_up.html')
from flask import Blueprint, render_template
from flask_login import login_required, current_user
from models.users import User

# Create a blueprint to handle different routes within the web page
site_views = Blueprint('site_views', __name__, static_folder='static', template_folder='templates', static_url_path='/static')

@site_views.route('/')
@site_views.route('/home/<user_id>')
def home_page(user_id=None):
    user = None
    if user_id is not None:
        user = User.query.get(user_id)
    return render_template('home.html', user=user)

@site_views.route('/houses/<user_id>')
@login_required
def house_page(user_id):
    user = User.query.get(user_id)
    return render_template('House.html', user=current_user, user_id=user_id)

@site_views.route('/about')
def about_page():
    return render_template('about.html', user=None)

@site_views.route('/sign_up')
def sign_page():
    return render_template('sign_up.html', user=None)

@site_views.route('/log-in')
def log_in():
    return render_template('log_in.html', user=None)

@site_views.route('/properties')
def all_properties():
    return render_template('view_properties.html', user=None)
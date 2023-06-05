from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/views')

from views.house import *
from views.sign_up import *
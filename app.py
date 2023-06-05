from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from views.routes import site_views
from views import app_views
from views.house import db
from views.sign_up import db

# A flask application instance
app = Flask(__name__)

# This configuration establishes a connection between the database and the flask app
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://end_user:password@localhost:3306/house_hunter'

# Register the app_views blueprint
app.register_blueprint(site_views, url_prefix='')

#Register the views blueprint
app.register_blueprint(app_views, url_prefix='')

# Register the Flask app with SQLAlchemy
db.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)
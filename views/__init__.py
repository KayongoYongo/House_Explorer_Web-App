from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Creating a database object
db = SQLAlchemy()

def create_app():
    # Create a flask application instance
    app = Flask(__name__)

    # This configuration establishes a connection between the database and the flask app
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://end_user:password@localhost:3306/house_hunter'

    # Initialize the database
    db.init_app(app)

    from views.routes import  site_views
    from views.sign_up import users_blueprint
    from views.house import house_blueprint
    from views.log_in import login_blueprint

    # Register the blueprints
    app.register_blueprint(site_views, url_prefix='')
    app.register_blueprint(users_blueprint, url_prefix='')
    app.register_blueprint(house_blueprint, url_prefix='')
    app.register_blueprint(login_blueprint, url_prefix='')

    return app
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin
from views.file_upload import UPLOAD_FOLDER

# Creating a database object
db = SQLAlchemy()

def create_app():
    # Create a flask application instance
    app = Flask(__name__)

    # This configuration establishes a connection between the database and the flask app
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://end_user:password@localhost:3306/house_hunter'

    # This provides session security and protect against tampering of cookies and other data
    app.config['SECRET_KEY'] = 'bonoko and friends'

        # configuring the upload folder 
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

    # Initialize the database
    db.init_app(app)

    # Import the blueprints from their modules
    from views.routes import  site_views
    from views.sign_up import users_blueprint
    from views.property import property_blueprint
    from views.all_properties import display_all_blueprint
    from views.log_in import login_blueprint
    from views.log_out import logout_blueprint

    # Register the blueprints
    app.register_blueprint(site_views, url_prefix='')
    app.register_blueprint(users_blueprint, url_prefix='')
    app.register_blueprint(property_blueprint, url_prefix='')
    app.register_blueprint(display_all_blueprint, url_prefix='')
    app.register_blueprint(login_blueprint, url_prefix='')
    app.register_blueprint(logout_blueprint, url_prefix='')

    # Create an instance of LoginManager
    login_manager = LoginManager()
    # page to redirect if user is not logged in
    login_manager.login_view = 'site_views.log_in'
    # Initialize the login manager
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        from models.users import User
        return User.query.get(id)

    return app

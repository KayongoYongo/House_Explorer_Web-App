from flask import Flask
from views.routes import site_views

# A flask application instance
app = Flask(__name__)

# Register the app_views blueprint
app.register_blueprint(site_views, url_prefix='')

if __name__ == '__main__':
    app.run(debug=True)

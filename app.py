from flask import Flask
from views import create_app

# Create the app object
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
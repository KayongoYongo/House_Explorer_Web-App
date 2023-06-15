from flask import Flask
from views import create_app

# Create the app object
app = create_app()

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)

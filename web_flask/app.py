#!/usr/bin/python3

from flask import Flask
from flask import render_template, url_for


app = Flask(__name__, static_folder='static', static_url_path='/static')

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/houses')
def house_page():
    return render_template('House.html')

@app.route('/about')
def about_page():
    return render_template('About.html')

@app.route('/sign in')
def sign_page():
    return render_template('sign.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

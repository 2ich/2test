
# A very simple Flask Hello World app for you to get started with...

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Flask! <br> <a href="wibble">click to wibble</a>'

@app.route('/wibble')
def wibble():
    return 'wibble wibble <a href="/">to / page</a>'


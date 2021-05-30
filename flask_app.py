
# A very simple Flask Hello World app for you to get started with...

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Flask! <hr> Its a third commit <a href="third">useless page<a>'

@app.route('/third')
def third_commit():
    return 'just a page i added on my third commit'

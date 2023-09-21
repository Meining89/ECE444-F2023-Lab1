from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)

#'<h1>Hello World!</h1>'
#'<h1>Hello, {}!</h1>'.format(name)
'''
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/')
def index():
    return '<h1>Hello Meg!</h1>'
'''

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name = name)

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/')
def index():
    return render_template('index.html', current_time=datetime.utcnow()) 
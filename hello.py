from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(_name_)
bootstrap = Bootstrap(app)

#'<h1>Hello World!</h1>'
#'<h1>Hello, {}!</h1>'.format(name)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name = name)
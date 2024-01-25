#!/usr/bin/python3
"""Starts a flask applicatioon.

The application listens on 0.0.0.0, port 5000
Routes:
    /: Displays 'Hello HBNB!'
    /hbnb: Displays "HBNB"
    /c/<text>: Displays C followed by the value of the text variable
    /python/<text>: display “Python ”, followed by the value of 
                    the text variable
    /number/<n>: display “n is a number” only if n is an integer
    /number_template/<n>: display a HTML page only if n is an integer:
                    H1 tag: “Number: n” inside the tag BODY
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Displays Hello HBNB!"""
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays HBNB!"""
    return 'HBNB!'

@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """Displays C followed by the value of the text variable"""
    text = text.replace('_', ' ');
    return 'C {}'.format(text)

@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text="is cool"):
    """Displays Python followed by the value of the text variable"""
    text = text.replace('_', ' ');
    return 'Python {}'.format(text)

@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """display “n is a number” only if n is an integer"""
    return "{} is a number".format(n)

@app.route('/number_template/<int:n>', stric_slashes=False)
def number_template(n):
    """display a HTML page only if n is an integer"""
    return render_tempalate('templates/5-number.html', number=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

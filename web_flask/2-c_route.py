#!/usr/bin/python3
""" script that starts a Flask web application """
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ hello HBNB function """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def slash_hbnb():
    """ function tied down to /hbnb """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def route_argument(text):
    """ function dealing with route argument passed

    Args:
        text (string): argument passed from the url
    """
    if '_' in text:
        result = text.replace('_', ' ')
        return f"C {result}"
    else:
        return "C " + text


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

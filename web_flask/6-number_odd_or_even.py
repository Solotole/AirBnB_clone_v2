#!/us_/bin/python3
""" script that starts a Flask web application """
from flask import Flask, render_template
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


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_default_argument(text):
    """ default argument
    Args:
        text (string): text to be accompanied
        on the HTTP responce
    """
    if '_' in text:
        result = text.replace('_', ' ')
        return f"Python {result}"
    else:
        return "Python " + text


@app.route('/number/<int:n>', strict_slashes=False)
def nuber_or_not(n):
    """ deterining if number or not

    Args:
        n (int): number to be printed
    """
    if isinstance(n, int):
        return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def template_number(n):
    """ Rendering html output """
    if isinstance(n, int):
        return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even(n):
    """ function to confirm odd of even

    Args:
        n (int): number to consider whether odd or even
    """
    if n % 2 != 0:
        determinant = 'odd'
    if n % 2 == 0:
        determinant = 'even'
    return render_template(
        '6-number_odd_or_even.html',
        n=n,
        determinant=determinant
        )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

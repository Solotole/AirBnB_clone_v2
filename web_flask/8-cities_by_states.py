#!/usr/bin/python3
""" accessing data from sql database """
from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.teardown_appcontext
def teardown_db_session(error):
    """ clossing a session """
    storage.close()


@app.route("/cities_by_states", strict_slashes=False)
def cities_states():
    """ retrieving and displaying cities of a
        state the data
    """
    states = storage.all('State')
    return render_template('8-cities_by_states.html', states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")

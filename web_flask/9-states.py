#!/usr/bin/python3
""" accessing data from sql database """
from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.teardown_appcontext
def teardown_db_session(error):
    """ clossing a session """
    storage.close()


@app.route('/states', strict_slashes=False)
def state():
    """Displays a html page with states"""
    states = storage.all(State)
    return render_template('9-states.html', states=states, way='all')


@app.route("/states/<id>", strict_slashes=False)
def states_by_id():
    """ retrieving and displaying cities of a
        state the data
    """
    for state in storage.all(State).values():
        if state.id == id:
            return render_template('9-states.html', states=state, way='id')
    return render_template('9-states.html', states=state, way='none')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")

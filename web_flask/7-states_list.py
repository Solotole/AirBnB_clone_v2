#!/usr/bin/python3
""" accessing data from sql database """
from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.teardown_appcontext
def teardown_db_session(error):
    """ clossing a session """
    storage.close()


@app.route("/states_list", strict_slashes=False)
def acquiring_displaying():
    from models.state import State
    """ retrieving and sorting the data """
    states = storage.all('State')
    sorted_states = sorted(states.values(), key=lambda state: state.name)
    return render_template('7-states_list.html', states=sorted_states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")

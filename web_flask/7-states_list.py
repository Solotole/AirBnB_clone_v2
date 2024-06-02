#!/usr/bin/python3
""" accessing data from sql database """
from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.teardown_appcontext
def teardown_db_session(exception):
    """ clossing a session """
    storage.close()


@app.route("/states_list", strict_slashes=False)
def acquiring_displaying():
    """ retrieving and sorting the data """
    states = storage.all("State")
    return render_template('7-states_list.html', states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")

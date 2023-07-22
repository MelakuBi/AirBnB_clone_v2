#!/usr/bin/python3
""" Task 10. States and State """
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route('/states')
@app.route('/states/<id>')
def states(id=None):
    states = list(storage.all(State).values())
    state_id = 0
    if id is not None:
        my_dict = storage.all(State)
        states = list(my_dict.values())
        key = "State.{}".format(id)
        if key in my_dict:
            state_id = 1
            states = [my_dict[key]]
        else:
            state_id = 2
    return render_template("9-states.html", states=states,
                           state_id=state_id, id=id)


@app.teardown_appcontext
def to_close(err):
    """ close app context """
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

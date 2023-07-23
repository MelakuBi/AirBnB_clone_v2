#!/usr/bin/python3
""" Task 12. HBNB is alive! """
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place
app = Flask(__name__)


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    states = list(storage.all(State).values())
    amenities = list(storage.all(Amenity).values())
    places = list(storage.all(Place).values())
    return render_template("100-hbnb.html",
                           states=states,
                           amenities=amenities,
                           places=places)


@app.teardown_appcontext
def to_close(err):
    """ close app context """
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

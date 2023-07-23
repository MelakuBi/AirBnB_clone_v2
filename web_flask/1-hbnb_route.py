#!/usr/bin/python3
""" Task 1. HBNB """
from flask import Flask
my_app = Flask(__name__)


@my_app.route("/", strict_slashes=False)
def my_root():
    return "Hello HBNB!"


@my_app.route("/hbnb", strict_slashes=False)
def my_hbnb():
    return "HBNB"

if __name__ == "__main__":
    my_app.run(host="0.0.0.0", port=5000)

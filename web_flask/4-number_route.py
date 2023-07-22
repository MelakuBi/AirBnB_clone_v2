#!/usr/bin/python3
""" Task 4. Is it a number? """
from flask import Flask
my_app = Flask(__name__)


@my_app.route("/", strict_slashes=False)
def my_root():
    return "Hello HBNB!"


@my_app.route("/hbnb", strict_slashes=False)
def my_hbnb():
    return "HBNB"


@my_app.route("/c/<text>", strict_slashes=False)
def my_c(text):
    return "C {}".format(text.replace("_", " "))


@my_app.route("/python", strict_slashes=False)
@my_app.route("/python/<text>", strict_slashes=False)
def my_python(text="is_cool"):
    return "Python {}".format(text.replace("_", " "))


@my_app.route("/number/<int:n>", strict_slashes=False)
def my_number(n):
    return "{} is a number".format(n)


if __name__ == "__main__":
    my_app.run(host="0.0.0.0", port=5000)

#!/usr/bin/env python3
"""
My first Flask app
"""
# Note, capital letters since, Invalid constant name "app" (invalid-name)
# https://stackoverflow.com/questions/10815549/pylint-showing-invalid-variable-name-in-output

# Import
from flask import Flask, render_template
from person import Person

APP = Flask(__name__)

PERSON_OBJECT = Person("Nicklas", "Envall", "21")

# Make it easier to debug
APP.debug = True
APP.config.update(
    PROPAGATE_EXCEPTIONS=True
)

@APP.route("/")
def main():
    """ Main route """
    return render_template("index.html")

@APP.route("/about")
def about():
    """ About route """
    return render_template("about.html", person=PERSON_OBJECT)

@APP.route("/uppgift1")
def uppgift1():
    """ uppgift1 route """
    return render_template("uppgift1.html")

if __name__ == "__main__":
    APP.run()

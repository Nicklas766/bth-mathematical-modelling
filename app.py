#!/usr/bin/env python3
"""
My first Flask app
"""
# Note, capital letters since, Invalid constant name "app" (invalid-name)
# https://stackoverflow.com/questions/10815549/pylint-showing-invalid-variable-name-in-output

# Import
from flask import Flask, render_template
from person import Person

app = Flask(__name__)

PERSON_OBJECT = Person("Nicklas", "Envall", "21")

# Make it easier to debug
app.debug = True
app.config.update(
    PROPAGATE_EXCEPTIONS=True
)

@app.route("/")
def main():
    """ Main route """
    return render_template("index.html")

@app.route("/about")
def about():
    """ About route """
    return render_template("about.html", person=PERSON_OBJECT)

@app.route("/uppgift1")
def uppgift1():
    """ uppgift1 route """
    return render_template("uppgift1.html")

@app.route("/centrala")
def centrala():
    """ centrala route """
    return render_template("centrala.html")

@app.route("/montecarlo")
def montecarlo():
    """ centrala route """
    return render_template("montecarlo.html")

@app.errorhandler(404)
def page_not_found(e):
    """
    Handler for page not found 404
    """
    #pylint: disable=unused-argument
    return "Flask 404 here, but not the page you requested."


@app.errorhandler(500)
def internal_server_error(e):
    """
    Handler for internal server error 500
    """
    #pylint: disable=unused-argument
    import traceback
    return "<p>Flask 500<pre>" + traceback.format_exc()

if __name__ == "__main__":
    app.run()

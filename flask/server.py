from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined


app = Flask(__name__)
app.jinja_env.undefined = StrictUndefined
app.jinja_env.auto_reload = True

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

# List of jobs in the application form
JOBS = [
	"Software Engineer", "Product Manager", "QA Engineer", "Data Scientist", "Engineering Evangelist",
]

# YOUR ROUTES GO HERE
@app.route('/')
def start_here():
	"""Displays Homepage."""
	return render_template("index.html")

@app.route('/application-form')
def application():
	"""Job selection page for user."""
	return render_template("application-form2.html", jobs = JOBS)

@app.route('/application-success', methods=["POST"])
def succes():
	""" Takes in inputs from user and serves confirmation page."""
	firstname = request.form.get("firstname")
	lastname = request.form.get("lastname")
	salary = float(request.form.get("salary"))
	position = request.form.get("position")

	return render_template("application-response.html", firstname = firstname, 
														lastname = lastname,
														salary = salary,
														position = position)

if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")

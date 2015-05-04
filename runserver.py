# -*- coding: utf-8 -*-
"""
	Interview.runserver
	~~~~~~~~~~~~~~~~~~~
"""
from application.controllers.main_controller import *
from application.controllers.profile_controller import *
from application.controllers.registration_controller import *
from application.controllers.not_found_controller import *
from flask import Flask, request, session

app = Flask(__name__)
app.debug = True
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

# Route 
@app.route("/", methods=["GET","POST"])
def index():
	"""
	This is index page!
	"""
	obj = Main(request)
	return obj.show()
	# return render_template("index.html")
@app.route("/registration", methods=["GET","POST"] )
def registration():
	"""
	This is registration page!
	"""
	obj = Registration(request)
	return obj.show()

@app.errorhandler(404)
def not_found_page(error):
	"""
	This is not foud page!
	"""
	obj = Not_Found()
	return obj.show()

if __name__ == "__main__":
	app.run()










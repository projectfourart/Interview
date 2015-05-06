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
	obj = Main()

	if request.method == "POST":
		if 'button_auth' in request.form: # if click button auth_user
			if len(request.form['username']) != 0 and len(request.form['password']) != 0: # validation
				obj.auth_user(request)
		if 'button_reg' in request.form:
			obj.reg_user(request)

	elif request.method == "GET":
		if request.args.get('drop') and request.args.get('drop') != "":
			obj.delete_user(request)
	
	obj.get_list_all_user()
	return obj.show()



@app.route("/registration" )
def registration():
	"""
	This is registration page!
	"""
	obj = Registration()
	return obj.show()

@app.route("/about_pro")
def about():
	pass
@app.route("/contact")
def contact():
	pass
@app.errorhandler(404)
def not_found_page(error):
	"""
	This is not foud page!
	"""
	obj = Not_Found()
	return obj.show()

if __name__ == "__main__":
	app.run()










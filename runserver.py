# -*- coding: utf-8 -*-
"""
	Interview.runserver
	~~~~~~~~~~~~~~~~~~~
"""
from application.controllers.main_controller import Main
from application.controllers.profile_controller import Profile
from application.controllers.registration_controller import Registration
from application.controllers.not_found_controller import Not_Found
from application.controllers.about_controller import About
from application.controllers.contact_controller import Contact
from flask import Flask, request, session, redirect, url_for

app = Flask(__name__)
app.debug = True
app.secret_key = "ass234jlk234nlui23j4l23k4j"

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
				obj.user.auth_user(request)
		if 'button_reg' in request.form:
			obj.user.reg_user(request)
		if 'id' in request.form and 'data' in request.form:
			obj.user.add_active_question(request) 

	elif request.method == "GET":
		if request.args.get('drop_id') and request.args.get('drop') != "":
			obj.user.delete_user(request.args.get('drop_id')) 
		elif request.args.get('drop_all') and request.args.get('drop') != "":
			obj.user.delete_all_user() 
			
		elif request.args.get('exit') == "True":
			obj.user.exit()
	
	# obj.user.get_list_all_user()
	return obj.show()



@app.route("/registration" )
def registration():
	"""
	This is registration page!
	"""
	obj = Registration()
	return obj.show()

@app.route("/profile/<int:id>")
def profile(id):
	"""
	This is profile page!
	"""

	obj = Profile()
	return obj.show(id)

@app.route("/about_pro")
def about():
	""" 
	This is about page!
	"""
	obj = About()
	return obj.show()

@app.route("/contact")
def contact():
	"""
	This is contact page!
	"""
	obj = Contact()
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










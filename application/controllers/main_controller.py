#! -*- coding: utf-8 -*-
"""
	Interview.application.controllers.main_controller
	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
from application.model.model import *
from application.views.main_view import *
from application.user.user import User
from flask import redirect, url_for

class Main(object):

	def __init__(self):
		self.__model = Model()
		self.__view = MainView()
		self.user = User()

	def show(self):
		# data = self.get_list_all_user() # default show old list user
		data = self.user.get_list_all_user()
		return self.__view.render(data)



	# def add_person(self,request):
	# 	if request.method == "POST":
	# 		if 'button_person' in request.form:
	# 			if (len(request.form["name_new_person"]) != 0 and len(request.form["surname_new_person"]) != 0):
	# 				name_person = request.form["name_new_person"]
	# 				surname_person = request.form["surname_new_person"]
	# 				self.model.AddNewPerson(name_person,surname_person)

	# def delete_person(self, request):
	# 	drop_index = request.args.get("drop")
	# 	self.model.DropPerson(drop_index)


	# def user_auth(self, request):
	# 	if 'username' in request.form and 'password' in request.form:
	# 		if self.model.IsExistsUser('Users',request.form['username'], request.form['password']):
	# 			session["username"] = request.form['username']
	# 			session["password"] = request.form['password']
	# 			self.__session = session
	# 			return redirect(url_for('index'))






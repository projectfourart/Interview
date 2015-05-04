#! -*- coding: utf-8 -*-
"""
	Interview.application.controllers.main_controller
	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
from application.model.model import *
from application.views.main_view import *
from flask import session, redirect, url_for

class Main(object):
	__session = None
	def __init__(self, request):
		self.model = Model()
		self.view = MainView()
		if request.method == "POST":
			self.user_auth(request)
			self.add_person(request)
			#...
		elif request.method == "GET":
			self.delete_person(request)
			#...


	def add_person(self,request):
		if request.method == "POST":
			if 'button_person' in request.form:
				if (len(request.form["name_new_person"]) != 0 and len(request.form["surname_new_person"]) != 0):
					name_person = request.form["name_new_person"]
					surname_person = request.form["surname_new_person"]
					self.model.AddNewPerson(name_person,surname_person)
	def delete_person(self, request):
		drop_index = request.args.get("drop")
		self.model.DropPerson(drop_index)

	def user_auth(self, request):
		if 'username' in request.form and 'password' in request.form:
			if self.model.IsExistsUser('Users',request.form['username'], request.form['password']):
				session["username"] = request.form['username']
				session["password"] = request.form['password']
				self.__session = session
				return redirect(url_for('index'))



	def show(self):
		data = self.model.getAllListPerson('Person')
		return self.view.render(data, session = self.__session)



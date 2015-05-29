#! -*- coding: utf-8 -*-
"""
	Interview.application.user
	~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
from application.model.model import Model
from application.configuration import TABLE_USERS
from flask import redirect, url_for, session
from application.configuration import ADMIN_NAME, ADMIN_PASSWORD

class User(object):
	
	def __init__(self):
		self.__model = Model()

	def auth_user(self, request):
		username = request.form['username']
		password = request.form['password']
		if username == ADMIN_NAME and password == ADMIN_PASSWORD:
			session['username'] = username
			session['type'] = 'admin'
			# session['id'] = None
		else:

			result = self.__model.IsExistsUser(TABLE_USERS, username, password)
			if result:
				if result[0] == password:
					session['username'] = username
					session['type'] = result[1]
					session['id'] = result[2]

	def AddSourses(self,id_src):
		self.__model.AddSRC(id_src)

	def add_active_question(self, request):
		id_user = request.form['id']
		text = request.form['data']
		self.__model.add_question(id_user, text)

	def exit(self):
		session.pop("admin", None)
		session.pop("username", None)
		redirect(url_for("index"))

	def reg_user(self, request):
		name = request.form['name']
		surname = request.form['surname']
		email = request.form['email']
		login = request.form['login']
		password = request.form['password']
		password_repeat = request.form['password_repeat']

		if password != password_repeat: return False # validation

		values = {'table_name':TABLE_USERS, 'name': name,'surname': surname, 'email':email, 'login':login, 'password': password, 'visible':"true", 'status': 'false','type':'user'}
		self.__model.AddUser(values)



	def delete_all_user(self):
		if session['admin'] == True:
			self.__model.DropAllUser()


	def delete_user(self, id):
		if session['admin'] == True:
			self.__model.DropPerson(id)
		

	def get_list_all_user(self):
		return self.__model.getAllListPerson(TABLE_USERS)

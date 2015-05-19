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
	# array_mondey = [u'--',u' Січень', u'Лютий', u'Березень', u'Квітень',u'Травень', u'Червень', u'Липень', u'Серпень',u'Вересень',u'Жовтень',u'Листопад',u'Грудень']
	
	def __init__(self):
		self.__model = Model()

	def auth_user(self, request):
		username = request.form['username']
		password = request.form['password']
		if self.__model.IsExistsUser(TABLE_USERS, username, password):
			session['username'] = username
			redirect(url_for("index"))
		if username == ADMIN_NAME and password == ADMIN_PASSWORD:
			session['admin'] = True
			session['username'] = "Admin"
			redirect(url_for("index"))



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
		brithish_day = str (request.form['day'] + ":0"+str( int(request.form['mondey']) )+":" + str(int(request.form['year']) + 1980)) # hard code
		role = str(request.form['role'])
		login = str(request.form['login'])
		
		if password != password_repeat: return False # validation
		values = {'table_name':TABLE_USERS, 'name': name,'surname': surname, 'brithish_day':brithish_day, 'email':email, 'password': password,'role': role,'visible':"true", 'login':login, 'status': 'false'}
		self.__model.AddUser(values)



	def delete_all_user(self):
		if session['admin'] == True:
			self.__model.DropAllUser()


	def delete_user(self, id):
		if session['admin'] == True:
			self.__model.DropPerson(id)
		

	def get_list_all_user(self):
		return self.__model.getAllListPerson(TABLE_USERS)

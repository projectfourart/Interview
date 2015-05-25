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
		data = self.__model.getAllSourses()
		users = []
		users_id = []
		for i in data:
			if i[3] != None:
				# users.append(i[3].split(':'))
				
				test = []
				test_id = []
				for j in i[3].split(':'):
					test.append(self.__model.getNameUser(j))
					test_id.append(self.__model.getIndexPerson("Users", j))
				users.append( test	)
				users_id.append( test_id)

			else:
				users.append([])
				users_id.append([])
		array_other = []
		for i in data:
			array_other.append(list(i))

		i = 0
		while i < len(array_other):
			array_other[i][3] = users[i]
			i += 1
		if session:
			interview = self.getAllSoursesUsers(users_id)
		else:
			interview = []
		return self.__view.render(array_other, interview)

	def getAllSoursesUsers(self, users_id):
		id_user = session['id']


		data = self.__model.getAllSoursesUsers(id_user)

		array_other = []
		for i in data:
			array_other.append(list(i))

		# print array_other


		k = 0
		for i in array_other:
			if i[2] != None:
				dump = str(i[2])[:-1].split(':')
				test = []
				for j in dump:
					test.append(self.__model.getIndexPerson("Users", j)[0])	
				array_other[k][2] = test
			k += 1	

		return array_other




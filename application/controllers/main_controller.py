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
		for i in data:
			if i[3] != None:
				# users.append(i[3].split(':'))
				
				test = []
				for j in i[3].split(':'):
					test.append(self.__model.getNameUser(j))
				users.append( test	)

			else:
				users.append([])
		new = []
		for i in data:
			new.append(list(i))

		i = 0
		while i < len(new):
			new[i][3] = users[i]
			i += 1
		return self.__view.render(new)



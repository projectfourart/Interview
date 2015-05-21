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
		data = self.user.get_list_all_user()
		return self.__view.render(data)



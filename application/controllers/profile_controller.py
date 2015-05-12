#! -*- coding: utf-8 -*-
"""
	Interview.application.controllers.main_controller
	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

from application.model.model import *
from application.views.view_profile import ViewProfile
from application.user.user import User
from flask import redirect, url_for
from application.configuration import *

class Profile(object):
	def __init__(self):
		self.__model = Model()
		self.__view = ViewProfile()

	def show(self, index):
		dump = self.__model.getIndexPerson(TABLE_USERS, index)
		return self.__view.render(dump)
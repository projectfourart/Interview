#! -*- coding: utf-8 -*-
"""
	Interview.application.controllers.about_controller
	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
from application.model.model import Model
from application.views.view_about import AboutView

class About(object):

	def __init__(self):
		self.__model = Model()
		self.__view = AboutView()
	def show(self):
		return self.__view.render()


#! -*- coding: utf-8 -*-
"""
	Interview.application.controllers.contact_controller
	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
from application.model.model import Model
from application.views.view_contact import ContactView

class Contact(object):

	def __init__(self):
		self.__model = Model()
		self.__view = ContactView()
	def show(self):
		return self.__view.render()


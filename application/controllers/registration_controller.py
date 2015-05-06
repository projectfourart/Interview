#! -*- coding: utf-8 -*-
"""
	Interview.application.controllers.registraion_controller
	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
from application.model.model import *
from application.views.registration_view import *

class Registration(object):
	def __init__(self):
		self.model = Model()
		self.view = RegView()



	def show(self):
		return self.view.render()


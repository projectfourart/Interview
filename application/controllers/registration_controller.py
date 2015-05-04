#! -*- coding: utf-8 -*-
"""
	Interview.application.controllers.registraion_controller
	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
from application.model.model import *
from application.views.registration_view import *

class Registration(object):
	def __init__(self, request):
		self.model = Model()
		self.view = RegView()
		if request.method == "POST":
			self.registration(request)


	def show(self):
		return self.view.render()

	def registration(self, request):
		self.model.AddUser(request)
		# print request.form


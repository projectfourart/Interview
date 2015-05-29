#! -*- coding: utf-8 -*-
"""
	Interview.application.views.main_view
	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
# from application.views.main_view import *
from flask import render_template
from application.model.model import Model
class MainView(object):
	def __init__(self):
		self.__model = Model()

	def render(self, data, interview):
		sourses = self.__model.getAllSourses()
		return render_template("index.html", data=data, interview = interview, sourses = sourses)


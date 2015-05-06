#! -*- coding: utf-8 -*-
"""
	Interview.application.views.main_view
	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
# from application.views.main_view import *
from flask import render_template

class MainView(object):
	def __init__(self, data=[]):
		self.data = data

	def render(self, data):
		return render_template("index.html", data=data)


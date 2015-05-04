#! -*- coding: utf-8 -*-
"""
	Interview.application.views.view_404
	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
from application.views.main_view import *
from flask import render_template

class View_404(object):
	def __init__(self, data=[]):
		self.data = data

	def render(self):
		return render_template("404.html")


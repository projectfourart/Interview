#! -*- coding: utf-8 -*-
"""
	Interview.application.views.registration_view
	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
from application.views.main_view import *
from flask import render_template

class RegView(object):
	def __init__(self):
		pass

	def render(self):
		return render_template("registration.html")



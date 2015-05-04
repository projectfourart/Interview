#! -*- coding: utf-8 -*-
"""
	Interview.application.controllers.not_found_controller
	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
from application.model.model import *
from application.views.view_404 import *

class Not_Found(object):
	def __init__(self):
		self.model = Model()
		self.view = View_404()
	def show(self):
		return self.view.render()

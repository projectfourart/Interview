#! -*- coding: utf-8 -*-
"""
	Interview.application.views.view_profile
	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
from flask import render_template
class ViewProfile(object):
	"""
		This is  profile view!
	"""
	def render(self, data, question, active_question):
		return render_template("base_profile.html", data = data, question = question, active = active_question)


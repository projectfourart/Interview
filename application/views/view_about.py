#! -*- coding: utf-8 -*-
"""
	Interview.application.views.view_about
	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
from flask import render_template

class AboutView(object):
	def render(self):
		return render_template("about_page.html")


#! -*- coding: utf-8 -*-
"""
	Interview.application.views.view_contact
	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
from flask import render_template

class ContactView(object):
	def render(self):
		return render_template("contact_page.html")


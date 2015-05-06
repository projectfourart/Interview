#! -*- coding: utf-8 -*-
"""
	Interview.application.user
	~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
from application.model.model import *
from application.configuration import * 
from flask import redirect, url_for, session

class User(object):
	def __init__(self):
		self.__model = Model()
	def auth_user(self, request):
		username = request.form['username']
		password = request.form['password']
		if self.__model.IsExistsUser(TABLE_USERS, username, password):
			session['username'] = username
			redirect(url_for("index"))
	def exit(self):
		session.pop("username", None)
		redirect(url_for("index"))

	def reg_user(self, request):
		print "reg_user"
	def delete_user(self, request):
		print "delete_user"
	def get_list_all_user(self):
		print "get_alls"
	# 	return self.__model.getAllListPerson('Users')
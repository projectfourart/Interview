#! -*- coding: utf-8 -*-
"""
	Interview.application.sourses
	~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
from application.model.model import Model
from application.configuration import TABLE_USERS
from flask import redirect, url_for, session
from application.configuration import ADMIN_NAME, ADMIN_PASSWORD

class Sourses(object):
	
	def __init__(self):
		self.__model = Model()
	def deleteSoursesId(self, id_src):
		self.__model.dropSrcIndex(id_src)
	def addNewSrc(self, name, text):
		self.__model.addSrc(name, text)
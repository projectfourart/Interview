#! -*- coding: utf-8 -*-
"""
	Interview.application.views.main_view
	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
# from application.views.main_view import *
from flask import render_template
from application.model.model import Model
from application.user.user import User

class MainView(object):
	def __init__(self):
		self.__model = Model()
		self.user = User()

	def render(self, data, interview):
		sourses = self.__model.getAllSourses()
		interviewter = self.__model.getAllInterviewter()
		array = []
		for team in interviewter:
			array.append(list(team))
		# for obj in array:
			# print self.user.getReqirment(team[0])[1]
			# array.append('test')
		i = 0
		while (i < len(array)):
			array[i].append(self.user.getReqirment(array[i][0]))
			# print self.user.getReqirment(array[i][0])
			i += 1
		# print array
		users = self.user.get_list_all_user()
		return render_template("index.html",user=users, data=data, interview = interview, sourses = sourses, interviewter=array)


#! -*- coding: utf-8 -*-
"""
	Interview.application.user
	~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
class User(object):

	def auth_user(self, request):
		print "auth_user"
	def reg_user(self, request):
		print "reg_user"
	def delete_user(self, request):
		print "delete_user"
	def get_list_all_user(self):
		print "get_alls"
	# 	return self.__model.getAllListPerson('Users')
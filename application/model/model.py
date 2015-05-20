#! -*- coding: utf-8 -*-
"""
	Interview.application.model.model
	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
from application.configuration import *
from ConfigParser import ConfigParser
import MySQLdb
import re

class Model(object):
	__connect = None
	__cursor = None
	def __init__(self):
			self.__connect = MySQLdb.connect(host = HOST, user = USER, passwd = PASSWORD, db = DATABASE, charset = CODING )
			self.__cursor = self.__connect.cursor()

	def getAllListPerson(self, table_name):
		sql = " SELECT `id`,`name`,`surname`,`brithish_day`,`status` FROM `"+table_name+"` WHERE `visible` =  'true' "
		self.__cursor.execute(sql)
		return self.__cursor.fetchall()

	def getIndexPerson(self, table, index):
		sql = "SELECT * FROM `%(table)s` WHERE  `id` = '%(index)s' " % {"table":table, "index": index}
		self.__cursor.execute(sql)
		return self.__cursor.fetchall()

	def IsExistsUser(self, table_name, user, password):
		sql = " SELECT `password` FROM `"+table_name+"` WHERE `name` = '"+user+"' "
		self.__cursor.execute(sql)

		try:
			if self.__cursor.fetchall()[0][0] == password:
				return True
		except IndexError:
			return False
		else:
			return False
	def add_question(self,id_user, text):
		sql = "UPDATE `Users` SET `quesition` = \'%s\', `status` = 'true' WHERE `id` = \'%s\' " % (text, id_user)
		self.__cursor.execute(sql)
		self.__connect.commit()

	def getQuestionAll(self):
		sql = "SELECT * FROM %s" % (TABLE_QUESTION)
		self.__cursor.execute(sql)
		return self.__cursor.fetchall()	

	# def AddNewPerson(self, name, surname):
	# 	sql = " INSERT INTO `Person` (`name`, `surname`) VALUES ( '%s' , '%s') " % (name, surname)
	# 	self.__cursor.execute(sql)
	# 	self.__connect.commit()
	def get_active_question(self, id_user):
		sql = "SELECT `quesition` FROM `Users` WHERE `id`  = \'%s\' " % (id_user)
		self.__cursor.execute(sql)
		result = str(self.__cursor.fetchall()[0][0])
		# print result
		index =  re.findall(r"(\d+)", result)
		array = []
		for i in index:
			self.__cursor.execute('SELECT `body` FROM `%s` WHERE `id` = \'%s\'' %  (TABLE_QUESTION, i))
			array.append(self.__cursor.fetchall()[0][0])
		return array

	def DropPerson(self, index_person):
		sql = "UPDATE `%(table_name)s` SET `visible` = 'false' WHERE `id` = '%(id)s' " % {"table_name":TABLE_USERS,"id":index_person}
		self.__cursor.execute(sql)
		self.__connect.commit()

	def DropAllUser(self):
		sql = "TRUNCATE TABLE %s" % TABLE_USERS
		self.__cursor.execute(sql)
		self.__connect.commit()

	def AddUser(self, values):
		sql = "INSERT INTO `%(table_name)s` (`name`,`surname`,`brithish_day`,`email`,`password`,`role`,`login`,`visible`,`status`) VALUES ('%(name)s','%(surname)s','%(brithish_day)s','%(email)s','%(password)s','%(role)s','%(login)s','%(visible)s','%(status)s') " % values
		self.__cursor.execute(sql)
		self.__connect.commit()






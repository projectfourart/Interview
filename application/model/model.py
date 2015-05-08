#! -*- coding: utf-8 -*-
"""
	Interview.application.model.model
	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
import MySQLdb
from application.configuration import *

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


	# def AddNewPerson(self, name, surname):
	# 	sql = " INSERT INTO `Person` (`name`, `surname`) VALUES ( '%s' , '%s') " % (name, surname)
	# 	self.__cursor.execute(sql)
	# 	self.__connect.commit()

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






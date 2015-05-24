#! -*- coding: utf-8 -*-
"""
	Interview.application.model.model
	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
from application.configuration import *
from flask import session
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
		sql = " SELECT `id`,`name`,`surname`,`status` FROM `"+table_name+"` WHERE `visible` =  'true' "
		self.__cursor.execute(sql)
		return self.__cursor.fetchall()

	def getIndexPerson(self, table, index):
		sql = "SELECT * FROM `%(table)s` WHERE  `id` = '%(index)s' " % {"table":table, "index": index}
		self.__cursor.execute(sql)
		return self.__cursor.fetchall()

	def IsExistsUser(self, table_name, user, password):
		sql = " SELECT `password`,`type`,`id` FROM `"+table_name+"` WHERE `login` = '"+user+"' "
		self.__cursor.execute(sql)
		try:
			return self.__cursor.fetchall()[0]
		except IndexError:
			return False

	def getNameUser(self,id):
		sql = "SELECT `login` FROM `Users` WHERE `id` = \'%s\'" % (id)
		self.__cursor.execute(sql)
		try:
			return self.__cursor.fetchall()[0][0]
		except IndexError:
			return []


		# return self.__cursor.fetchall()[0][0]


	def getAllSourses(self):
		sql = "SELECT * FROM `Sourses` "
		self.__cursor.execute(sql)
		return self.__cursor.fetchall()

	def add_question(self,id_user, text):
		sql = "UPDATE `Users` SET `quesition` = \'%s\', `status` = 'true' WHERE `id` = \'%s\' " % (text, id_user)
		self.__cursor.execute(sql)
		self.__connect.commit()

	def AddSRC(self, id_src):
		data = self.getAllSourses()
		users = []
		for i in data:
			if i[3] != None:
				# users.append(i[3].split(':'))
				test = []
				for j in i[3].split(':'):
					test.append(self.getNameUser(j))
				users.append( test	)

			else:
				users.append([])

		id_user = session['id']
		if session['username'] not in users[int(id_src)-1]:
			fild_uresr = data[int(id_src)-1][3]

			if fild_uresr != None:
				users = str(fild_uresr)+"%s:"  % id_user
			else:

				users = "%s:" % id_user

			sql_src = "UPDATE `Sourses` SET `users` = '%(users)s' WHERE `id` = \'%(id_src)s\' " % {"users":users,"id_src":id_src}
			self.__cursor.execute(sql_src)
			self.__connect.commit()

		
			

	def getQuestionAll(self):
		sql = "SELECT * FROM %s" % (TABLE_QUESTION)
		self.__cursor.execute(sql)
		return self.__cursor.fetchall()	

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
		sql = "INSERT INTO `%(table_name)s` (`name`,`surname`,`email`,`login`,`password`,`visible`,`status`,`type`) VALUES ('%(name)s','%(surname)s','%(email)s','%(login)s','%(password)s','%(visible)s','%(status)s','%(type)s') " % values
		self.__cursor.execute(sql)
		self.__connect.commit()






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
		sql = " SELECT * FROM `"+table_name+"` "
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


	def AddNewPerson(self, name, surname):
		sql = " INSERT INTO `Person` (`name`, `surname`) VALUES ( '%s' , '%s') " % (name, surname)
		print sql
		self.__cursor.execute(sql)
		self.__connect.commit()

	def DropPerson(self, index_person):
		sql = "DELETE  FROM `Person` WHERE `id` = '%s' " % index_person
		self.__cursor.execute(sql)
		self.__connect.commit()

	def AddUser(self, resquest):
		# print resquest.form

		username = resquest.form['name']
		surname = resquest.form['surname']
		british_day = [resquest.form['data_day'], resquest.form['data_year']]
		email = resquest.form['email']
		password = resquest.form['password']		
		repeat_password = resquest.form['repeat_password']
		role = resquest.form['role']
		# print username, surname, british_day, email, password, repeat_password, role
		# sql = " INSERT INTO `Users` (`name`,`surname`,`brithish_day`,`email`,`password`, `role`) VALUES ('%s','%s','%s','%s','%s','%s') " % ( username, surname, ""+british_day[1]+"", email, password, role )
		sql = " INSERT INTO `Users` (`name`,`surname`,`brithish_day`,`email`,`password`, `role`) VALUES ('%s','%s','%s','%s','%s','%s') " % ( username, surname, ""+british_day[1]+"", email, password, role )

		self.__cursor.execute(sql)
		self.__connect.commit()






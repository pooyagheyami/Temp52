#In The name of God
#!/usr/bin/env python
# -*- codnig: utf-8 -*-


from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy.orm import sessionmaker
#from sqlalchemy import Table,Column,Integer,String,Text

from Config.Init import *

class Get:
	def __init__(self, DBF, engine):
		self.DBF = DBF

		if engine == 'sqlite':
			self.myengin = create_engine('sqlite:///'+self.DBF, echo=True)
		if engine == 'postgresql':
			self.myengin = create_engine('postgresql://scott:tiger@localhost/'+self.DBF)
			# psycopg2
			#self.myengin = create_engine('postgresql+psycopg2://scott:tiger@localhost/mydatabase')
			# pg8000
			#self.myengin = create_engine('postgresql+pg8000://scott:tiger@localhost/mydatabase')
		if engine == 'mysql':
			self.myengin = create_engine('mysql://scott:tiger@localhost/'+self.DBF)
			# mysqlclient (a maintained fork of MySQL-Python)
			#self.myengin = create_engine('mysql+mysqldb://scott:tiger@localhost/foo')
			# PyMySQL
			#self.myengin = create_engine('mysql+pymysql://scott:tiger@localhost/foo')
		if engine == 'oracle':
			self.myengin = create_engine('oracle://scott:tiger@127.0.0.1:1521/'+self.DBF)
			# self.myengin = create_engine('oracle+cx_oracle://scott:tiger@tnsname')
		if engine == 'sqlserver':
			#self.myengin = create_engine('mssql+pymssql://scott:tiger@hostname:port/'+self.DBF)
			self.myengin = create_engine('mssql+pyodbc://scott:tiger@mydsn')

		meta = MetaData()


	def openSQL(self, sqlfile):
		with open(sqlfile) as f:
			self.alltext = f.readlines()
		return  self.alltext

	def GetFromSql(self):
		with self.myengin.connect() as conn :
			session = sessionmaker()
			result = conn.execute(self.alltext[0])
			conn.close()
			#conn.commit()
		return result

	def GetFromString(self, sqlstring):
		with self.myengin.connect() as conn:
			result = conn.execute(sqlstring)
			return result.fetchall()





class Post:
	def __init__(self, DBF, Data, engine):
		self.DBF = DBF
		self.Data = Data

		if engine == 'sqlite':
			self.myengin = create_engine('sqlite:///'+self.DBF, echo=True)
		if engine == 'postgresql':
			self.myengin = create_engine('postgresql://scott:tiger@localhost/'+self.DBF)
		if engine == 'mysql':
			self.myengin = create_engine('mysql://scott:tiger@localhost/'+self.DBF)
		if engine == 'oracle':
			self.myengin = create_engine('oracle://scott:tiger@127.0.0.1:1521/'+self.DBF)

	def Addrecord(self):
		pass

	def Updaterecord(self):
		pass

	def Deleterecord(self):
		pass
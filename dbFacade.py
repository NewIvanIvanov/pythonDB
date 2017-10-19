import MySQLdb
import json

#current database by default
dataBase = "SQL"

class MongoDB():
	'''for future purpose'''
	pass

class SQL():
	'''define our connection to SQL_DB and gives data to it as user object'''

	def check(self):
		'''for test case'''
		print("SQL")

	def connectSQL_DB(self):
		'''creating DB connect'''
		connect = MySQLdb.connect(host='localhost', user='root', passwd='', db='test_project')
		return connect

	def update(self, data):
		'''updating record'''
		conn = self.connectSQL_DB()
		cursor = conn.cursor()
		cursor.execute("UPDATE {0} SET name='{2}', surname='{3}', age={4} WHERE id={1}".format(data.table, data.id, data.name, data.surname, data.age))
		print('DB updated')
		conn.commit()
		conn.close()

	def select(self, data):
		'''selecting record '''
		conn = self.connectSQL_DB()
		cursor = conn.cursor()
		cursor.execute("SELECT * from {0} WHERE id={1}".format(data.table, data.id))
		print('DB selected')
		row = cursor.fetchall()
		print(row)
		open("jsondata.json", 'a').close()
		somedict = {
			"table" : "user",
			"fields" : {
				"id" : "5",
				"name" : "Robby",
				"surname" : "Murrey",
				"age" : "50"
			},
			"method" : "select"
		}
		with open("jsondata.json", 'w') as d:
			json.dump(somedict, d)

		conn.close()

	def delete(self, data):
		'''deleting record '''
		conn = self.connectSQL_DB()
		cursor = conn.cursor()
		cursor.execute("DELETE from {0} where id={1}".format(data.table, data.id))
		conn.commit()
		print('record deleted')
		conn.close()

	def insert(self, data):
		'''inserting record '''
		conn = self.connectSQL_DB()
		cursor = conn.cursor()
		cursor.execute("INSERT INTO {0} (id, name, surname, age) VALUES ({1}, '{2}', '{3}', {4})".format(data.table, "DEFAULT", data.name, data.surname, data.age))
		conn.commit()
		print('record inserted')
		conn.close()




	def run(self, data):
		'''check out action method with database'''
		self.method = data.method
		if self.method == "update":
			self.update(data)
		elif self.method == "select":
			self.select(data)
		elif self.method == "delete":
			self.delete(data)
		elif self.method == "insert":
			self.insert(data)
		else: print("Methot not defined...")


class Facade():
	'''DB choise'''
	def dbChoise(self):
		
		if dataBase == "SQL": return SQL()
		if dataBase == "MongoDB" : return Mongo()





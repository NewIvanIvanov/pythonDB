
class User():
	'''define our user with id, name, surname and age'''
	def __init__(self, table, data, method):
		self.table = table
		self.id = data["id"]
		self.name = data["name"]
		self.surname = data["surname"]
		self.age = data["age"]
		self.method = method




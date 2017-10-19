import MySQLdb
connect = MySQLdb.connect(host='localhost', user='root', passwd='')
cursor = connect.cursor()
cursor.execute("CREATE DATABASE test_project")
connect.commit()
connect.close()

connect = MySQLdb.connect(host='localhost', user='root', passwd='', db='test_project')
cursor = connect.cursor()
cursor.execute("""CREATE TABLE user(
	id int(10) NOT NULL AUTO_INCREMENT, 
	name varchar(50),
	surname varchar(50),
	age smallint(3),
	PRIMARY KEY(id))""")
print('Table created')
connect.commit()
connect.close()



	

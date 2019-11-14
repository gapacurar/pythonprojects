import mysql.connector
# connect to MySQL database server
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="tnceicsnt#333"
)
# create a new database instance on mySql server
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE persons")
#display all existing databases on mySQL server
#mycursor.execute("SHOW DATABASES")
# for x in mycursor:
#  print(x)
# connect to new created database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="tnceicsnt#333",
  database="persons"
)
mycursor = mydb.cursor()
# create table in database persons
mycursor.execute("CREATE TABLE PERSONS (cnp VARCHAR(13), name VARCHAR(50), surname VARCHAR(50), city_code VARCHAR(3))")
mycursor.execute("CREATE TABLE CITIES (city_code VARCHAR(3), name VARCHAR(50), region_code VARCHAR(3))")
mycursor.execute("CREATE TABLE REGIONS (region_code VARCHAR(3), name VARCHAR(50))")
# insert rows in persons table
sql = "INSERT INTO PERSONS (cnp, name, surname, city_code) VALUES (%s, %s, %s, %s)"
val = ('1234567890123', 'Peter', 'Peterson','1')
val1 = ('1234567890321', 'Amy', 'Peterson','2')
mycursor.execute(sql, val)
mydb.commit()
mycursor.execute(sql, val1)
mydb.commit()
# insert rows in cities table
sql = "INSERT INTO CITIES (city_code, name, region_code) VALUES (%s, %s, %s)"
val = ('1', 'New York', '1')
val1 = ('2', 'San Francisco', '2')
mycursor.execute(sql, val)
mydb.commit()
# insert regions in cities table
sql = "INSERT INTO REGIONS (region_code, name) VALUES (%s, %s)"
val = ('1', 'New York')
mycursor.execute(sql, val)
val1 = ('2', 'California')
mycursor.execute(sql, val)
mydb.commit()
# display inserted rows in table persons
print("PERSONS TABLE")
print("=============")
mycursor.execute("SELECT * FROM PERSONS")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)
# display inserted rows in table cities
print("CITIES TABLE")
print("=============")
mycursor.execute("SELECT * FROM CITIES")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)
# display inserted rows in table regions
print("REGIONS TABLE")
print("=============")
mycursor.execute("SELECT * FROM REGIONS")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)
# delete all rows from tables
mycursor.execute("DELETE FROM PERSONS")
mycursor.execute("DELETE FROM CITIES")
mycursor.execute("DELETE FROM REGIONS")
mydb.commit()
print("ALL TABLES CONTENT WERE DELETED")
print("=============")
for x in myresult:
  print(x)
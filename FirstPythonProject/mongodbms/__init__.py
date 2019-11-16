#conecting to a mongo DB
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# create DB personas
mydb = myclient["personas"]
print(mydb)
#print(myclient.list_database_names())
# create or return the table/collection named personas
mycollection = mydb["personas"]
#insert one document/row into personas collection and return an id of inserted values
#mydict = {"name":"Jimmy","surname":"Carter","city_code":1}
#x = mycollection.insert_one(mydict)
#print("Inserted a document/row into already existing collection/database: "+str(x.inserted_id))
#insert more documents/rows into personas collection specifing their IDs explicitely in persons collection/table
#mylistofpersons = [
#  { "person_id": 1, "name": "John", "surname": "Doe", "city_id":1},
#  { "person_id": 2, "name": "Jane", "surname": "Doe", "city_id":2}
#]
#y = mycollection.insert_many(mylistofpersons)
#print list of the _id values of the inserted documents:
#print("Inserted a list of documents/rows into already existing collection/database - persons: "+ str( y.inserted_ids))
#insert more documents/rows, specifing their IDs explicitely, in cities collection/table
#mylistofcities = [
#  { "city_id": 1, "name": "New York", "region_id":1},
#  { "city_id": 2, "name": "San Francisco", "region_id":2}
#]
#z = mycollection.insert_many(mylistofcities)
#print list of the _id values of the inserted documents:
#print("Inserted a list of documents/rows into already existing collection/database - cities: " + str( z.inserted_ids))
#insert more documents/rows, specifing their IDs explicitely, in regions collection/table
#mylistofregions = [
#  { "region_id": 1, "name": "New York"},
#  { "region_id": 2, "name": "California"}
#]
#t = mycollection.insert_many(mylistofregions)
#print list of the _id values of the inserted documents:
#print("Inserted a list of documents/rows into already existing collection/database - regions: " + str( t.inserted_ids))
#find information from existing collections and documents - similar to select
# select * from equivqlent
for x in mycollection.find():
# select with complete where clause in SQL
  print("Select * from personas DB, all tables, meaning repetitive find(): "+str(x))
for y in mycollection.find({},{ "person_id": 1, "name": 1, "surname": 1, "city_id":1 }):
  print("Select from personas DB, all tables, using find() paramaters: "+str(y))
# select all records with surname Doe
myquery = { "surname": "Doe" }
mydoc = mycollection.find(myquery)
for x in mydoc:
  print("Selected rows having surname=Doe : "+str(x))
# use regex for selection - all documents/rows starting with J
myquery = { "name": { "$regex": "^J" } }
mydoc = mycollection.find(myquery)
for x in mydoc:
  print("Rows filtered using regex ^J"+str(x))
mydoc = mycollection.find(myquery).sort("name",-1)
for x in mydoc:
  print("Rows filtered using regex ^J sorted descending following name"+str(x))
# update all names with Noah
newvalues = { "$set": { "name": "Noah" } }
mycollection.update_one(myquery, newvalues)
for x in mydoc:
  print("Rows filtered using regex ^J sorted descending following name"+str(x))
#print "personas" after the update:
for x in mycollection.find():
  print(x)  
# clean all collections/tables
q = mycollection.delete_many({})
print("documents/rows from collection personas deleted: "+str(q)  )
# distroy or drop whole collection
mycollection.drop()
#conecting to a mongo DB
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["personas"]
print(mydb)
#print(myclient.list_database_names())
mycollection = mydb["personas"]
#insert one document/row and return an id of inserted values
mydict = {"name":"Jimmy","surname":"Carter","city_code":1}
x = mycollection.insert_one(mydict)
print("Inserted a document/row into already existing collection/database: "+str(x.inserted_id))
#insert more documents specifing their IDs explicitely in persons collection/table
mylistofpersons = [
  { "person_id": 1, "name": "John", "surname": "Doe", "city_id":1},
  { "person_id": 2, "name": "Jane", "surname": "Doe", "city_id":2}
]
y = mycollection.insert_many(mylistofpersons)
#print list of the _id values of the inserted documents:
print("Inserted a list of documents/rows into already existing collection/database - persons: "+ str( y.inserted_ids))
#insert more documents specifing their IDs explicitely in cities collection/table
mylistofcities = [
  { "city_id": 1, "name": "New York", "region_id":1},
  { "city_id": 2, "name": "San Francisco", "region_id":2}
]
z = mycollection.insert_many(mylistofcities)
#print list of the _id values of the inserted documents:
print("Inserted a list of documents/rows into already existing collection/database - cities: " + str( z.inserted_ids))
#insert more documents specifing their IDs explicitely in regions collection/table
mylistofregions = [
  { "region_id": 1, "name": "New York"},
  { "region_id": 2, "name": "California"}
]
t = mycollection.insert_many(mylistofregions)
#print list of the _id values of the inserted documents:
print("Inserted a list of documents/rows into already existing collection/database - regions: " + str( t.inserted_ids))

#conecting to a mongo DB
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["persons"]
#print(mydb)
mycollection = mydb["persons"]
#insert one document/row and return an id of inserted values
mydict = {"name":"Jimmy","surname":"Carter","city_code":1}
x = mycollection.insert_one(mydict)
print(x.inserted_id)
#insert more documents specifing their IDs explicitely
mylist = [
  { "_id": 1, "name": "John", "surname": "Doe", "city_code":1},
  { "_id": 2, "name": "Jane", "surname": "Doe", "city_code":2}
]
y = mycollection.insert_many(mylist)
#print list of the _id values of the inserted documents:
print(y.inserted_ids)
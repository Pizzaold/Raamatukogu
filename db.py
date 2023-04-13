from pymongo import MongoClient

def get_database(name):

   CONNECTION_STRING = "mongodb+srv://Pizzaold:Pizzaold25@library.onhnimp.mongodb.net/test"
 
   client = MongoClient(CONNECTION_STRING)
 
   return client[name]

dbname_lib = get_database("Librarys_collection")
dbname_mem = get_database("Members_collection")
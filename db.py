from pymongo import MongoClient
"""
File with the database connection.
Used to connect to the database.
"""

def get_database(name):
   """Get the database."""	

   CONNECTION_STRING = "mongodb+srv://Pizzaold:Pizzaold25@library.onhnimp.mongodb.net/test" # Because its nothing sensitive, I just put the connection string here.
 
   client = MongoClient(CONNECTION_STRING)
 
   return client[name]

dbname_lib = get_database("Librarys_collection")
dbname_mem = get_database("Members_collection")
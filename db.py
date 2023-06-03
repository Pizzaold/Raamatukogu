from pymongo import MongoClient
"""
File with the database connection.
Used to connect to the database.
"""

def get_database(name):
   """Get the database."""	

   CONNECTION_STRING = "LIBRARY CONNECTION STRING GOES HERE"
 
   client = MongoClient(CONNECTION_STRING)
 
   return client[name]

dbname_lib = get_database("Librarys_collection")
dbname_mem = get_database("Members_collection")
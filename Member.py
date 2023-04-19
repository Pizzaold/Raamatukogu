from pymongo import MongoClient
from db import dbname_mem

class Members:

    def add_member(self, name):
        dbname_mem.members.insert_one({
            "name": name,
            "rentables": [],
        })

    def test(self, name):
        dbname_mem.members.find_one({"name": name}) 


if __name__ == '__main__':
    member = Members()
    member.add_member("Aimar")
    member.test("Aimar")
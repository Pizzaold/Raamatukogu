from pymongo import MongoClient
from db import dbname_lib
"""
File with the item class.
Used to add items to the library database.
"""


class Item:
    type = ["book", "magazine", "dvd"]

    def add_item(self, library_name, item_name, amount, type):
        if type not in Item.type:
            print("Invalid type")
        else:
            dbname_lib.library.update_one(
                {"name": library_name},
                {
                    "$push": {
                        "type": type,
                        "name": item_name,
                        "amount": amount,
                        "popularity": 0,
                    }
                },
            )

    def test(self, name):
        dbname_lib.rentables.find_one({"name": name})

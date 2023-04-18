import datetime
from Object import Item
from pymongo import MongoClient
from db import dbname_lib
from db import dbname_mem
"""
File with the Library class.
Used to for all main library functions.
"""


class Library:

    return_time = datetime.datetime.strptime(datetime.datetime.now().strftime("%Y-%m-%d"), "%Y-%m-%d") + datetime.timedelta(days=21)

    def __init__(self, libary_name):
        """init :)"""
        self.type = ["book", "magazine", "dvd"]
        self.library_name = libary_name

    def create_library(self):
        dbname_lib.librarys.insert_one(
            {
                "name": self.library_name,
                "rentables": [],
            }
        )

    def add_item(self, item_name, amount, type):
        """
        Add an item to the library database
        :param item_name: The name of the item
        :param amount: The amount of the item
        :param type: The type of the item
        :return: None
        """
        if type not in self.type:
            print("Invalid type")
        else:
            dbname_lib.librarys.update_one(
                {"name": self.library_name},
                {
                    "$push": {
                        "rentables": {
                            "type": type,
                            "name": item_name,
                            "amount": amount,
                            "popularity": 0,
                        }
                    }
                },
            )

    def test(self):
        """Just some random test"""
        dbname_lib.librarys.find_one({"name": self.library_name})

    def rent(self, rentable, member):
        """
        Rent an item to a member, icrease the popularity of the item and decrease the amount of the item in library.
        :param rentable: The name of the rentable item
        :param member: The name of the member
        :return: None
        """
        item_type = dbname_lib.librarys.find_one({"name": self.library_name, 'rentables': {'$elemMatch': {'name': rentable}}})
        item_type = item_type['rentables'][0]['type']
        dbname_mem.members.update_one(
            {"name": member},
            {
                "$push": {
                    "rentables": {
                        "name": rentable,
                        "type": item_type,
                        "library": self.library_name,
                        "rent_our_date": datetime.datetime.strptime(datetime.datetime.now().strftime("%Y-%m-%d"), "%Y-%m-%d"),
                        "return_date": Library.return_time,
                    }
                }
            },
        )

        dbname_lib.librarys.update_one(
            {"name": self.library_name, "rentables.name": rentable},
            {
                "$inc": {"rentables.$.amount": -1},
            },
        )

        if dbname_lib.librarys.find_one({"name": self.library_name, "rentables.name": rentable})['rentables'][0]['popularity'] < 10:
            dbname_lib.librarys.update_one(
                {"name": self.library_name, "rentables.name": rentable},
                {
                    "$inc": {"rentables.$.popularity": +1},
                },
            )

    def see_rentables(self):
        """
        See the list of the rentable items in the library
        :return: None
        """
        rentables = []
        for rentable in dbname_lib.librarys.find({"name": self.library_name}):
            for rentable in rentable["rentables"]:
                rentables.append(rentable["name"])
        print("The list of the rentable items are: ")
        for rentable in rentables:
            print(rentable)
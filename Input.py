from Library import Library
from pymongo import MongoClient
from db import dbname_lib, dbname_mem

"""
File with the main function.
Used to start the program and get users input.
"""

# Get the list of the library
list_of_libraries = []
for library in dbname_lib.librarys.find():
    list_of_libraries.append(library["name"])

while True:
    new_or_old = input(
        "Do you want to create a new library or use an existing one? (new/old): "
    )

    if new_or_old == "new":
        library_name = input("Enter the name of the library: ")
        if library_name in list_of_libraries:
            print("This library already exists")
        else:
            library = Library(library_name)
            library.create_library()
            print("The library has been created")
    elif new_or_old == "old":
        print("The list of the libraries are: ")
        for library in list_of_libraries:
            print(library)
        library_name = input("Enter the name of the library: ")
        if library_name in list_of_libraries:
            library = Library(library_name)
            print("The library has been selected")
            print(f"The list of actions for {library_name} are: add, rent, see_rentables.")
            next_action = input("What is your next action? ")
            if next_action == "add":
                item_name = input("Enter the name of the item: ")
                amount = int(input("Enter the amount of the item: "))
                type = input("Enter the type of the item: ")
                library.add_item(item_name, amount, type)
                print("The item has been added")
            elif next_action == "rent":
                item_type = []
                members = []
                for rentable in dbname_lib.librarys.find({"name": library_name}):
                    for rentable in rentable["rentables"]:
                        item_type.append(rentable["name"])
                print("The list of the rentable items are: ")
                for rentable in item_type:
                    print(rentable)
                for member in dbname_mem.members.find():
                    members.append(member["name"])
                print("The list of the members are: ")
                for member in members:
                    print(member)
                rentable_name = input("Enter the name of the rentable item: ")
                if dbname_lib.librarys.find_one({"name": library_name, "rentables.name": rentable})['rentables'][0]['amount'] > 0:
                    if rentable_name in item_type:
                        member = input("Enter the name of the member: ")
                        library.rent(rentable_name, member)
                        print("The item has been rented out")
                    else:
                        print("This item does not exist")
                else:
                    print("This item is rented out")
            elif next_action == "see_rentables":
                library.see_rentables()
        else:
            print("This library does not exist")
    else:
        print("Invalid input")
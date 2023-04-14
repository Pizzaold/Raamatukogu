from Library import Library
from pymongo import MongoClient
from db import dbname_lib, dbname_mem

"""
This fail is used to get the input from the user
"""

# Get the list of the library
list_of_libraries = []
for library in dbname_lib.librarys.find():
    list_of_libraries.append(library["name"])

new_or_old = input(
    "Do you want to create a new library or use an existing one? (new/old): "
)

if new_or_old == "new":
    libary_name = input("Enter the name of the library: ")
    if libary_name in list_of_libraries:
        print("This library already exists")
        exit()
    else:
        library = Library(libary_name)
        library.create_libary()
        print("The library has been created")
elif new_or_old == "old":
    print("The list of the libraries are: ")
    for library in list_of_libraries:
        print(library)
    libary_name = input("Enter the name of the library: ")
    if libary_name in list_of_libraries:
        library = Library(libary_name)
        print("The library has been selected")
        next_action = input("Do you want to add a new item or rent out an item? (add/rent): ")
        if next_action == "add":
            item_name = input("Enter the name of the item: ")
            amount = int(input("Enter the amount of the item: "))
            type = input("Enter the type of the item: ")
            library.add_item(item_name, amount, type)
            print("The item has been added")
        elif next_action == "rent":
            item_type = []
            members = []
            for rentable in dbname_lib.librarys.find({"name": libary_name}):
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
            if rentable_name in item_type:
                member = input("Enter the name of the member: ")
                library.rent(rentable_name, member)
                print("The item has been rented out")
            else:
                print("This item does not exist")
                exit()
    else:
        print("This library does not exist")
        exit()
else:
    print("Invalid input")
    exit()


"""rentables_question = input(
    "Do you want to see our list of rentable books, magazines, DVDs? (yes/no): "
)

if rentables_question == "yes":
    print("Our rentable books, magazines and DVDs are:")
    for object in library.rentables:
        print(object)
elif rentables_question == "no":
    print("K.")
else:
    print("Invalid input")"""
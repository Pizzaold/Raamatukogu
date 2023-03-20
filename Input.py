from Library import Library
"""
This fail is used to get the input from the user
"""

# Get the list of the library
f = open("library.txt", "r")
list_of_libraries = f.readlines()
f.close()

new_or_old = input("Do you want to create a new library or use an existing one? (new/old): ")

if new_or_old == "new":
    name = input("Enter the name of the library: ")
    if name in list_of_libraries:
        print("This library already exists")
        exit()
    else:
        library = Library(name)
        library.add_library(name)
        print("The library has been created")
elif new_or_old == "old":
    print("The list of the libraries are: ")
    for library in list_of_libraries:
        print(library)
    name = input("Enter the name of the library: ")
    if name in list_of_libraries:
        library = Library(name)
        print("The library has been selected")
    else:
        print("This library does not exist")
        exit()
else:
    print("Invalid input")
    exit()
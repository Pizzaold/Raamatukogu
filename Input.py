from Library import Library
from Member import Member
"""
This fail is used to get the input from the user
"""

# Get the list of the library
f = open("Library.txt", "r")
list_of_libraries = f.readlines()
f.close()

# Get the list of the members
member_names = []
f = open("Members.txt", "r")
for line in f: # get list of members names
    member_names.append(line.split(",")[0].split(":")[1])
f.close()
print(member_names)

user_or_member = input("Are you a user or a member? (user/member): ") # Ask the user if he is a user or a member

if user_or_member == "user": # If the user is a user
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
elif user_or_member == "member": # If the user is a member
    new_or_old = input("Do you want to create a new member or use an existing one? (new/old): ") # ask the user if he wants to create a new member or use an existing one

    if new_or_old == "new":
        name = input("Enter the name of the member: ") # ask the user to enter the name of the member
        if name in member_names: # if the member already exists
            print("This member already exists")
            exit()
        elif name not in member_names: # if the member does not exist
            member = Member(name)
            member.add_member()
            print("The member has been created")
        else: # if the user enters an invalid input
            print("Invalid input")
            exit()
    elif new_or_old == "old": # if the user wants to use an existing member
        print("The list of the members are: ")
        for member in member_names: # print the list of the members
            print(member)
        name = input("Enter the name of the member: ")
        if name in member_names: # if the member exists
            member = Member(name)
            print("The member has been selected")
        elif name not in member_names: # if the member does not exist
            print("This member does not exist")
            exit()
        else: # if the user enters an invalid input
            print("Invalid input")
            exit()


rentables_question = input("Do you want to see our list of rentable books, magazines, DVDs? (yes/no): ")

if rentables_question == "yes":
    print("Our rentable books, magazines and DVDs are:")
    for object in library.rentables:
        print(object)
elif rentables_question == "no":
    print("K.")
else:
    print("Invalid input")
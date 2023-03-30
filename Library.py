"""
Library class is used to create a library object
"""
from datetime import date
from Objects import Book


class Library:
    def __init__(self, name):
        self.name = name
        self.members = open("members.txt", "r").readlines()
        self.rentables = open("rentable_objects", "r").readlines()

    def add_library(self, name):
        f = open("Library.txt", "a")
        f.write(self.name)
        f.close()

    def test(self):
        print(self.rentables)

    def rent(self, rentable, user):
        """Rent out a rentable object to user by adding it to members lib and removing one from library lib."""
        items = open("rentable_objects", "r+")
        offset = 0
        for item in items:
            item_name = item.split(",")[1]  # Find the name of the object
            if rentable.name == item_name:
                with open("members.txt", "r") as temp:  # Opens members.txt for reading
                    lines = temp.readlines()
                with open("members.txt", "w") as members:  # Opens members.txt for writing
                    for line in lines:
                        members.write(line)  # Writes line back to file
                        offset += len(line)  # Keep count of lines
                        if user in line:
                            line.strip("\n")
                            members.seek(offset - 1)  # Seek out the right place to write the new line
                            members.write(f"{rentable};{date.today()}:\n")  # Write the rented object to user lib
                with open("rentable_objects", "r") as temp:  # Open rentable_objects.txt for reading
                    lines = temp.readlines()
                with open("rentable_objects", "w") as objects:  # Open rentable_objects.txt for writing
                    for line in lines:
                        amount = line.split(",")[-1:]  # Finds the amount of available items
                        for x in amount:  # Makes list into str
                            amount = x
                        new_amount = int(amount) - 1  # New amount
                        if rentable.name in line:
                            amount_len = len(amount)  # Length of amount
                            temp = line[:-amount_len] + str(new_amount)  # New line without old amount
                            objects.write(temp)  # Writes edited amount back to file
                        else:
                            objects.write(line)  # Writes unedited lines back to file

    def return_object(self, rentable, member_name):
        """Temporary."""
        with open("members.txt", "r") as x:
            members = x.readlines()
        for member in members:
            items_rented = member.split("!")[1]
            name = member.split(",")[0]
            print(items_rented)
            if name == member_name:
                print("Pass1")
                if rentable.name in items_rented:
                    with open("members.txt", "r") as temp:
                        lines = temp.readlines()
                    with open("members.txt", "w") as file:
                        for line in lines:
                            if rentable.name in line:
                                print(rentable.name, "MNMN")
                                index = items_rented.find(f"{rentable.name};")
                                next_colon_index = items_rented.find(":", index)
                                new_string = "!" + items_rented[:index] + items_rented[next_colon_index + 1:]
                                print(new_string, "B")
                                new_line = member.split("!")[0] + new_string
                                print("Pass2")
                                file.write(new_line)
                            else:
                                file.write(line)


if __name__ == "__main__":
    book1 = Book("Lord of the rings")
    library1 = Library("Test")
    library1.test()
    #library1.rent(book1, "aimar")
    library1.return_object(book1, "aimar")
"""
Library class is used to create a library object
"""
from datetime import date
from Objects import Book

class Library:
    def __init__(self, name):
        self.name = name
        self.members = open("members.txt", "r").readlines()[1:]
        self.rentables = open("rentable_objects.txt", "r").readlines()

    def add_library(self, name):
        f = open("Library.txt", "a")
        f.write(self.name)
        f.close()

    def test(self):
        print(self.rentables)

    def rent(self, rentable, user):
        """Rent out a rentable object to user by adding it to members lib and removing one from library lib."""
        items = open("rentable_objects.txt", "r+")
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
                            members.write(f",{rentable};{date.today()}\n")  # Write the rented object to user lib
                with open("rentable_objects.txt", "r") as temp:  # Open rentable_objects.txt for reading
                    lines = temp.readlines()
                with open("rentable_objects.txt", "w") as objects:  # Open rentable_objects.txt for writing
                    for line in lines:
                        amount = line.split(",")[-1:]  # Finds the amount of available items
                        for item in amount:  # Makes list into str
                            amount = item
                        new_amount = int(amount) - 1  # New amount
                        if rentable.name in line:
                            temp = line[:-1] + str(new_amount)  # New line
                            objects.write(temp)  # Writes edited amount back to file
                        else:
                            objects.write(line)  # Writes unedited lines back to file







if __name__ == "__main__":
    book1 = Book("Lord of the rings")
    library1 = Library("Test")
    library1.test()
    library1.rent(book1, "aimar")
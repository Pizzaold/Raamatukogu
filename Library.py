"""
Library class is used to create a library object
"""
from datetime import date

class Library:
    def __init__(self, name):
        self.name = name
        self.members = open("members.txt", "r").readlines()[1:]
        self.rentables = open("rentable_objects", "r").readlines()

    def add_library(self, name):
        f = open("Library.txt", "a")
        f.write(self.name)
        f.close()

    def test(self):
        print(self.rentables)

    def rent(self, rentable_name, user):
        """Rent out a rentable object to user by adding it to members lib and removing one from library lib."""
        items = open("rentable_objects", "r+")
        offset = 0
        for item in items:
            item_name = item.split(",")[1]  # Find the name of the object
            if rentable_name == item_name:
                with open("members.txt", "r") as temp:  # Opens members for reading
                    lines = temp.readlines()
                with open("members.txt", "w") as members:  # Opens members for writing
                    for line in lines:
                        members.write(line)  # Writes line back to file
                        offset += len(line)  # Keep count of lines
                        if user in line:
                            line.strip("\n")
                            members.seek(offset - 1)  # Seek out the right place to write the new line
                            members.write(f",{rentable_name};{date.today()}\n")  # Write the rented object to user lib




if __name__ == "__main__":
    library1 = Library("Test")
    library1.test()
    library1.rent("Lord of the rings", "aimar")
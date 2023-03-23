"""
Library class is used to create a library object
"""

class Library:
    def __init__(self, name):
        self.name = name
        self.members = []
        self.rentables = open("rentable_objects", "r").readlines()

    def add_library(self, name):
        f = open("Library.txt", "a")
        f.write(self.name)
        f.close()

    def test(self):
        print(self.rentables)


if __name__ == "__main__":
    library1 = Library("Test")
    library1.test()
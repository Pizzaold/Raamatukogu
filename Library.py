"""
Library class is used to create a library object
"""

class Library:
    def __init__(self, name):
        self.name = name
        self.members = open("members", "r").readlines()[1:]
        self.rentables = open("rentable_objects", "r").readlines()

    def add_library(self, name):
        f = open("Library.txt", "a")
        f.write(self.name)
        f.close()

    def test(self):
        print(self.rentables)

    def rent(self):
        lines = open("members", "r")
        for line in lines:
            line.strip("\n")
            print(line)



if __name__ == "__main__":
    library1 = Library("Test")
    library1.test()
    library1.rent()
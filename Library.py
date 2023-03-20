"""
Library class is used to create a library object
"""

class Library:
    def __init__(self, name):
        self.name = name
        self.mebmers = []
        self.rentables = []

    def add_library(self, name):
        f = open("library.txt", "a")
        f.write(self.name)
        f.close()
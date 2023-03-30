class Book:

    def __init__(self, name):
        self.name = name
        rentable = True

    def add(self, amount):
        with open("rentable_objects.txt", "w") as objects:
            objects.write(f"book,{str(self)},{amount}")

    def __repr__(self):
        return self.name


class Magazine:

    def __init__(self, name):
        self.name = name
        rentable = True

    def __repr__(self):
        return self.name


class DVD:

    def __init__(self, name):
        self.name = name
        rentable = True

    def __repr__(self):
        return self.name


if __name__ == "__main__":
    book1 = Book("Lord of the rings")
    book1.add(2)

with open("rentable_objects.txt", "r") as object1:
    line = object1.readline()
    print(line)
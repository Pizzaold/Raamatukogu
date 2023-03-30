class Book:

    def __init__(self, name, amount, popularity):
        self.name = name
        self.amount = amount
        self.popularity = popularity
        rentable = True

    def __repr__(self):
        return self.name


class Magazine:

    def __init__(self, name, amount, popularity):
        self.name = name
        self.amount = amount
        self.popularity = popularity
        rentable = True

    def __repr__(self):
        return self.name


class DVD:

    def __init__(self, name, amount, popularity):
        self.name = name
        self.amount = amount
        self.popularity = popularity
        rentable = True

    def __repr__(self):
        return self.name
"""File for the Member class."""

class Member:
    def __init__(self, name):
        self.name = name
        self.librarys = []
        self.rented = []

    def add_member(self):
        """Add a member to the list of members."""
        with open("members.txt", "a") as file:
            file.write(f"name:{self.name}, librarys:{self.librarys}, rented:{self.rented}\n")

if __name__ == "__main__":
    member = Member("Joonas")
    member.add_member()

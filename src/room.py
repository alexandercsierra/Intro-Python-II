# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items):
        self.name = name
        self.description = description
        self.items = items
        self.n_to=None
        self.e_to=None
        self.s_to=None
        self.w_to=None

    def __str__(self):
        return f"{self.name}, {self.description}"

    def remove_item(self, current_item):
        del self.items[current_item]

    def add_item(self, current_item):
        self.items.append(current_item)

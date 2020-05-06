# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items, isLight, naturalLight):
        self.name = name
        self.description = description
        self.items = items
        self.isLight = isLight
        self.naturalLight = naturalLight
        self.n_to=None
        self.e_to=None
        self.s_to=None
        self.w_to=None

    def __str__(self):
        if self.isLight == True or self.naturalLight == True:
            return f"You have entered the {self.name}. {self.description}"
        else:
            return f"It's pitch black!"

    def remove_item(self, index):
        del self.items[index]

    def add_item(self, current_item):
        self.items.append(current_item)

    def illuminate(self):
        self.isLight = True
    
    def darken(self):
        self.isLight = False

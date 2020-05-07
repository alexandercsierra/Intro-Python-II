# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, current_room):
        self.current_room = current_room
        self.items = []
        self.money = 0

    def __str__(self):
        return f"current room is {self.currentRoom}"

    def move(self, direction):
        attribute = direction + "_to"
        if hasattr(self.current_room, attribute) and getattr(self.current_room, attribute) != None:
            return getattr(self.current_room, attribute)
        else:
            print("Can't go that way")
            return self.current_room

    def print_inv(self):
        print('\nYour inventory currently contains:\n')
        for item in self.items:
            print(item)
        print(f'\nWallet: {self.money}\n')

    def take_item(self, item):
        if item.name in self.current_room.items:
            self.items.append(item)
            item.on_take()
            self.current_room.remove_item(item.name) 
        else:
            print('Nothing by that name here')
        
    def drop_item(self, item):
        if item in self.items:
            index = self.items.index(item)
            item.on_drop() 
            self.current_room.add_item(item.name)      
            del self.items[index]  
        else:
            print("You don't have anything like that")

    def add_money(self, amount):
        self.money += amount
        
    def remove_money(self, amount):
        self.money -= amount

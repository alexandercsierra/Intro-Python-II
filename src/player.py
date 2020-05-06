# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, currentRoom):
        self.currentRoom = currentRoom
        self.items = []
        self.money = 0
    def __str__(self):
        return f"current room is {self.currentRoom}"
    def take_item(self, item):
        self.items.append(item)
    def leave_item(self, index):
        del self.items[index]  
    def add_money(self, amount):
        self.money += amount
    def remove_money(self, amount):
        self.money -= amount

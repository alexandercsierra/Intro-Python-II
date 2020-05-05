# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, currentRoom):
        self.currentRoom = currentRoom
    def __str__(self):
        return f"current room is {self.currentRoom}"
    

from colorama import init
from colorama import Fore, Back, Style


init(autoreset=True)

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.items = []
        self.money = 0
        self.moves = []

    def __str__(self):
        return f"current room is {self.currentRoom}"

    def move(self, direction):
        attribute = direction + "_to"
        if hasattr(self.current_room, attribute) and getattr(self.current_room, attribute) != None:
            return getattr(self.current_room, attribute)
        else:
            print(Fore.RED + "Can't go that way")
            return self.current_room

    def print_inv(self):
        print(Fore.CYAN + '\nYour inventory currently contains:')
        for item in self.items:
            print(item.name)
        print(Fore.YELLOW + f'Wallet: {self.money}\n')

    def take_item(self, item):
        if item.name in self.current_room.items:
            if hasattr(item, 'value'):
                self.money += item.value
            self.items.append(item)
            item.on_take()
            self.current_room.remove_item(item.name) 

        else:
            print('Nothing by that name here')
        
    def drop_item(self, item):
        if item in self.items:
            if hasattr(item, 'value'):
                self.money -= item.value
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

    def use_item(self, item):
        if item.name == self.current_room.correct_item:
            self.drop_item(item)
            self.current_room.success()
            self.current_room.remove_item(item.name)
        else:
            print(self.current_room.item_use_failure)

    def examine_item(self, item):
        if item in self.items or item.name in self.current_room.items:
            print(item)

    def go_back(self):
        opps = {
            'n':'s',
            's':'n',
            'e':'w',
            'w':'e'
        }
        if len(self.moves) > 1:
            return self.move(opps[self.moves[-1]])
        elif len(self.moves) == 1:
            return self.move(opps[self.moves[0]])
        else: 
            print(f"{Fore.RED}Sorry, you can't go back any more")
            return self.current_room
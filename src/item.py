from colorama import init
from colorama import Fore, Back, Style


init(autoreset=True)


class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f'{self.name}, {self.description}'

    def on_drop(self):
        print(f'You have dropped {self.name}')

    def on_take(self):
        print(Fore.GREEN + f'You have picked up {self.name}')
    



class Treasure(Item):
    def __init__(self, name, description, value):
        super().__init__(name, description)
        self.value = value
    
    def __str__(self):
        return f"{self.name} is worth ${self.value}"



class LightSource(Item):
    def __init__(self, name, description):
        super().__init__(name, description)

    def on_drop(self):
        print(f"{Fore.RED}It's not wise to drop your source of light!")

    



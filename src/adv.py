from room import Room
from player import Player
from item import Item
from item import Treasure
from item import LightSource
from inventory import inventory


# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", ['sword', 'ring'], True, True, "", ""),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", ['torch'], True, True, "ring", "You correctly used the ring"),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",[], True, True, "ring", "You toss the ring into the chasm. As it plunges, a the light grows until it fills the room. A new pathway opens to the north"),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",[], False, False, "", ""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",[], False, False, "", ""),

    'secret': Room("Secret Passage", """You spot a suspicious looking brick in the wall which comes loose, revealing a passage. Through the hole you see a glimmer of light. Opening a few more bricks you squeeze through to find a pile of gold lying on the floor.""",['gold'], False, False, "", ""),
}

item_list = {
    'sword': Item('sword', 'a big scary blade'),
    'ring': Item('ring', 'one ring to rule them all'),
    'gold': Treasure('gold', 'looks shiny', 10000),
    'diamond': Treasure('diamond', 'very nice cut', 1000),
    'torch': LightSource('torch', 'a beacon of light')
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']
room['treasure'].n_to = room['secret']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# # Write a loop that:
# #
# direction = None
# while direction != 'q':
#     # * Prints the current room name
#     # * Prints the current description (the textwrap module might be useful here).
#     # * Waits for user input and decides what to do.
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.



def adventure(): 
    player = Player(room['outside'])
    end = False
    win = False

    while end == False and win != True:
        if player.money > 10000:
            win = True
            break
        #darken or light the room depending on if the player has the torch in their inventory
        if item_list['torch'] in player.items:
            player.current_room.illuminate()
        else:
            player.current_room.darken()
 

        print(player.current_room)
        action = input('What would you like to do?\n\n')
        if action == "q":
            end = True

        #searching a room
        if action == 'search':
            player.current_room.search_room()
        #traveling between rooms
        if action == 'n' or action == 's' or action == 'e' or action == 'w':
            player.current_room = player.move(action)
        elif 'get' in action:
            split = action.split()
            selected = split[1]
            player.take_item(item_list[selected])
        elif 'drop' in action:
            split = action.split()
            selected = split[1]
            player.drop_item(item_list[selected])

        elif action in ['help', 'h', '?']:
            print("Travel or search by using 't' or 's'. Travel 'n' 's' 'e' or 'w' .\nGet an item with 'get [name of item]' and drop with 'drop [name of item]. Use 'q' or 'quit' to end the game.\n")
        elif action == 'inventory' or action == 'i':
            player.print_inv()

    if win == True:
        print("You've won!")
    elif end == True:
        print('Thanks for playing\n')


adventure()








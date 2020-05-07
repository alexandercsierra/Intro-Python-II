from room import Room
from player import Player
from item import Item
from item import Treasure
from item import LightSource
from search_room import search_room
from travel_to_room import travel_to_room
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
    'sword': Item('a sword', 'a big scary blade'),
    'ring': Item('the one ring', 'one ring to rule them all'),
    'gold': Treasure('pile of gold', 'looks shiny', 10000),
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
    room_name = 'outside'
    curr_room = room[room_name]
    player = Player(curr_room)
    end = False
    win = False
    playing = True

    # while playing == True and player.money < 10000:
    while end == False and win != True:
        
        if 'torch' in player.items:
            curr_room.illuminate()
        else:
            curr_room.darken()
        print(curr_room)
        print(player.current_room)
        # if player.money >= 10000:
        #     print('WINNING')
        #     win = True
        #     playing = False
        #     print(f'playing {playing}')
        action = input('Would you like to travel or search?\n\n')
        if action == "q":
            end = True
            # playing = False
        #searching a room
        if action == 'search' or action == 's':
            win = search_room(action, curr_room, player, item_list, win)
        #traveling between rooms
        elif action == 'travel' or action == 't':
            curr_room = travel_to_room(curr_room)
        elif action == 'help' or action == 'h':
            print('Type t or s to select travel or search. When traveling, type n s e or w to move in a cardinal direction.\nWhen searching, type "get" and the name of the item you would like to collect.\nType i to access inventory. While in your inventory, type "examine" and the name of the item to examine it,\nor "drop" and the name of the item to drop it.')
        elif action == 'inventory' or action == 'i':
            inventory(player, item_list, curr_room)
    if win == True:
        print("You've won!")
    elif end == True:
        print('Thanks for playing\n')


adventure()








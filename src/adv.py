from room import Room
from player import Player
from item import Item
from search_room import search_room
from travel_to_room import travel_to_room
from inventory import inventory

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", ['sword', 'ring']),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", []),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",[]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",[]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",[]),
}

item_list = {
    'sword': Item('a sword', 'a big scary blade'),
    'ring': Item('the one ring', 'one ring to rule them all')
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
    quit = False

    while quit == False:

        print(f'\nYou have entered the {curr_room.name}. {curr_room.description}')
        action = input('Would you like to travel or search?\n\n')
        if action == "q":
            # return print(f'Thanks for playing\n')
            quit = True
        #searching a room
        if action == 'search' or action == 's':
            search_room(action, curr_room, player, item_list)
        #traveling between rooms
        elif action == 'travel' or action == 't':
            curr_room = travel_to_room(curr_room)
        elif action == 'help' or action == 'h':
            print('Type t or s to select travel or search. When traveling, type n s e or w to move in a cardinal direciton. When searching, type the name of the item you would like to collect. Type i to access inventory.')
        elif action == 'inventory' or action == 'i':
            inventory(player, item_list, curr_room)
    print('Thanks for playing\n')


adventure()








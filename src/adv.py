from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", ['sword']),

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
    direction = None
    while direction != 'q':
        print(f'You have entered the {curr_room.name}. {curr_room.description}')
        # print(curr_room.name)
        # print(curr_room.description)
        action = input('Would you like to search the room?')
        if action == 'yes':
            print(f'you found {curr_room.items}')
            take = input(f'would you like to take the {curr_room.items}?')
            if take == 'yes':
                print(f'you have taken {curr_room.items}.')
                player.take_item(curr_room.items[0])
                print(f'your current inventory is {player.items}.')
        direction = input('Which direction shall you go?')
        if direction == 'n':
            if curr_room.n_to != None:
                curr_room = curr_room.n_to
            else: 
                print('THERE IS NOTHING TO THE NORTH')
        elif direction == 'e':
            # if hasattr(curr_room, 'e_to'):
            if curr_room.e_to != None:
                curr_room = curr_room.e_to
            else: 
                print('THERE IS NOTHING TO THE EAST')
        elif direction == 's':
            if curr_room.s_to != None:
                curr_room = curr_room.s_to
            else: 
                print('THERE IS NOTHING TO THE SOUTH') 
        elif direction == 'w':
            if curr_room.w_to != None:
                curr_room = curr_room.w_to
            else: 
                print('THERE IS NOTHING TO THE WEST')
        else:
            print('PLEASE ENTER either n s e or w TO MOVE OR q TO QUIT')
    print('thanks for playing')


adventure()

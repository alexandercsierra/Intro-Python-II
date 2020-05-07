from room import Room
from player import Player
from item import Item
from item import Treasure
from item import LightSource
from room_list import room
from item_list import item_list



# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']
room['workroom'].s_to = room['overlook']
room['secret'].s_to = room['treasure']




def adventure(): 
    name = input("What's your name?\n")
    player = Player(name, room['outside'])
    end = False
    win = False
    print(f'Welcome, treasure-hunter {player.name}. Riches lie within.')
    selected = None

    while end == False and win == False:

        #these rooms only available if correct item used
        if player.current_room.new_passage == True:
            if player.current_room.name == 'Grand Overlook':
                room['overlook'].n_to = room['workroom']
            if player.current_room.name == 'Treasure Chamber':
                room['treasure'].n_to = room['secret']



        #player wins if they have 10000 gold
        if player.money >= 10000:
            win = True
            break

        #darken or light the room depending on if the player has the torch in their inventory
        if item_list['torch'] in player.items:
            player.current_room.illuminate()
        else:
            player.current_room.darken()
 
        print('\n')
        if player.current_room.new_passage == True:
            print(player.current_room.alt_desc)
        else:
            print(player.current_room)
        action = input('What would you like to do?\n\n')
        split = action.split()
        
        #quitting the game
        if action == "q" or action == "quit":
            end = True
        #searching a room
        elif action == 'search':
            player.current_room.search_room()
        #traveling between rooms
        elif action == 'n' or action == 's' or action == 'e' or action == 'w':
            player.current_room = player.move(action)
        #item usage
        elif len(split) > 1:
            selected = split[1]
            if 'get' in action:
                player.take_item(item_list[selected])
            elif 'drop' in action:
                player.drop_item(item_list[selected])
            elif 'use' in action:
                player.use_item(item_list[selected])
            elif 'examine' in action:
                if selected != 'room':
                    player.examine_item(item_list[selected])
                else:
                    player.current_room.describe()
        elif action == 'examine':
                print("Be more specific. Examine what (item name or 'room')?")
        #open inventory
        elif action == 'inventory' or action == 'i':
            player.print_inv()
        #possible commands
        elif action in ['help', 'h', '?']:
            print("Travel 'n' 's' 'e' or 'w' .\nGet an item with 'get [name of item]' and drop with 'drop [name of item].\nUse an item with 'use [name of item]'.\nOpen inventory with 'i'.\nExamine the current room by typing 'examine room' or an item by typing 'examine [name of item]'.\nUse 'q' or 'quit' to end the game.\n")
        else:
            print("I don't understand what you mean. Use 'h' to see list of available options")

        

        

    if win == True:
        print(f"Congratulations, {player.name}! You've found the treasure and won!")
    elif end == True:
        print('Thanks for playing\n')


adventure()








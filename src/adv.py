from room import Room
from player import Player
from item import Item
from item import Treasure
from item import LightSource
from room_list import room
from item_list import item_list
from colorama import init
from colorama import Fore, Back, Style


init(autoreset=True)
# print(Fore.RED + 'some red text')
# print(Back.GREEN + 'and with a green background')
# print(Style.DIM + 'and in dim text')
# # print(Style.RESET_ALL)
# print('back to normal now')


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
room['tomb'].w_to = room['secret']


help_text = "Travel using:" + Fore.GREEN + " n s e w " + Style.RESET_ALL + " or " + Fore.GREEN + "b "+ Style.RESET_ALL + "to go back."+"\nSearch a room by typing "+ Fore.GREEN +"search"+ Style.RESET_ALL +"\nExamine the current room by typing"+ Fore.GREEN +" examine room "+ Style.RESET_ALL +" or an item by typing "+ Fore.GREEN +" examine [name of item]"+ Style.RESET_ALL +"\nGet an item with "+ Fore.GREEN +"get [name of item]"+ Style.RESET_ALL + " and drop with "+ Fore.GREEN +"drop [name of item]"+ Style.RESET_ALL + "\nUse an item with"+ Fore.GREEN +" use [name of item]"+ Style.RESET_ALL + "\nOpen inventory with"+ Fore.GREEN +" i"+ Style.RESET_ALL + "\nUse "+ Fore.RED +"q"+ Style.RESET_ALL + " or "+ Fore.RED +"quit"+ Style.RESET_ALL + " to end the game.\n"

def adventure(): 
    name = input("What's your name?\n")
    player = Player(name, room['outside'])
    end = False
    win = False
    print(Fore.BLUE + Back.BLACK + f'\nWelcome, treasure-hunter {player.name}. Riches lie within.')
    print("Type" + Fore.RED +" 'h'" + Style.RESET_ALL + " or " + Fore.RED + "'help' " + Style.RESET_ALL + "to see a list of possible commands\n")
    selected = None

    while end == False and win == False:

        #these rooms only available if correct item used
        if player.current_room.new_passage == True:
            if player.current_room.name == 'Grand Overlook':
                room['overlook'].n_to = room['workroom']
            if player.current_room.name == 'Treasure Chamber':
                room['treasure'].n_to = room['secret']
            if player.current_room.name == 'Secret Passage':
                room['secret'].e_to = room['tomb']




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
            print(f'{Fore.BLUE}{player.current_room.alt_desc}')
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
            player.moves.append(action)
        elif action == 'b' or action == 'back':
            player.current_room = player.go_back()
            if len(player.moves) > 0:
                del player.moves[-1]
        #item usage
        elif 'destroy' in action:
            print(Fore.BLUE + "Please don't.")
        elif 'jump' in action:
            print(Fore.BLUE + "You start hopping for some reason. Good thing no one's here to witness this.")
        elif len(split) > 1:
            selected = split[1]
            if selected in item_list:
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
            else:
                print(Fore.RED + "Not sure what you wanted. Try typing 'h' for a list of valid commands.")
        elif action == 'examine':
                print(Fore.RED + "Be more specific. Examine what (item name or 'room')?")
        #open inventory
        elif action == 'inventory' or action == 'i':
            player.print_inv()
        #possible commands
        elif action in ['help', 'h', '?']:
            print(help_text)
        else:
            print(Fore.RED + "I don't understand what you mean. Use 'h' to see list of available options")

        

        

    if win == True:
        print(Fore.YELLOW + f"Congratulations, {player.name}! You've found the treasure and won!")
    elif end == True:
        print(f'{Fore.GREEN}Thanks for playing\n')


adventure()








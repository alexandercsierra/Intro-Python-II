def search_room(action, curr_room, player, item_list, win):
     #searching the room
        #does the room have natural light or does the player have a torch or is the torch in the current room
        if curr_room.isLight == True or curr_room.naturalLight == True or 'torch' in curr_room.items:
            #if the room contains items
            if len(curr_room.items) > 0:   
                print('You have found:')             
                print(*curr_room.items)
                print('\n')
                take = input(f'Want to get an item?\n')
                #if the item typed in by user exists in the list
                if 'get' in take:
                    split = take.split()
                    selected = split[1]
                    act = split[0]
                    if act == 'get':
                        if selected in curr_room.items:
                            index = curr_room.items.index(selected)
                            item_list[selected].on_take()
                            player.take_item(curr_room.items[index])
                            curr_room.remove_item(index)
                            #if item is a treasure, add the value to the wallet. If new total exceeds win condition, print message
                            if hasattr(item_list[selected], 'value') == True:
                                if player.money + item_list[selected].value >= 10000:
                                    return True
                                else: 
                                    player.add_money(item_list[selected].value)
                        #player entered incorrect item name       
                        else: 
                            print('\nSorry, nothing by that name is here.\n')
                #player did not try to get
                else:
                    print('')
            #if the room is empty        
            else:
                print(f'\nYou found nothing. May as well move on.\n')
        #the room is too dark to see
        else: 
            print(f'\nGood luck finding anything in the dark...')


                
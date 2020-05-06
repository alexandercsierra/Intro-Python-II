def search_room(action, curr_room, player, item_list):
     #searching the room
        
            #if the room contains items
            if len(curr_room.items) > 0:   
                print('You have found:')             
                print(*curr_room.items)
                print('\n\n')
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
                        else: 
                            print('\nSorry, nothing by that name is here.\n')
                else:
                    print('')
            #if the room is empty        
            else:
                print(f'You found nothing. May as well move on.\n')

                
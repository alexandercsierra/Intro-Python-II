def inventory(player, item_list):
    print (f'wallet: {player.money}')
    if len(player.items) > 0:
        print('\nyour current inventory includes:')
        print(*player.items)
        drop = input('Examine or drop an item?\n')
        if 'examine' in drop or 'drop' in drop or 'use' in drop:
            split = drop.split()
            selected = split[1]
            act = split[0]
            if act == 'drop':
                if selected in player.items:
                    index = player.items.index(selected)
                    item_list[selected].on_drop()
                    player.leave_item(index)
                    player.current_room.add_item(selected)
                    print(f'current room items {player.current_room.items}')
                    print(f'inventory {player.items}')
                    #is the item a treasure? then remove value from the wallet on drop
                    if hasattr(item_list[selected], 'value') == True:
                                player.remove_money(item_list[selected].value)
            elif act == 'examine':
                if selected in player.items:
                    print('\n')
                    print(item_list[selected].description)
                    print('\n')
            elif act == 'use':
                # print('in use block')
                if selected in player.items:
                    if player.current_room.correct_item == selected:
                        player.current_room.success()
                    else:
                        player.current_room.failure()
        else:
            print('exited inventory')
    else:
        print("\n you aren't carrying anything right now")
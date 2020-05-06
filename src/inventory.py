def inventory(player, item_list, curr_room):
    if len(player.items) > 0:
        print('\nyour current inventory includes:')
        print(*player.items)
        drop = input('Examine or drop an item?\n')
        if 'examine' in drop or 'drop' in drop:
            split = drop.split()
            selected = split[1]
            act = split[0]
            if act == 'drop':
                if selected in player.items:
                    index = player.items.index(selected)
                    item_list[selected].on_drop()
                    player.leave_item(index)
                    curr_room.add_item(selected)
                    print(f'current room items {curr_room.items}')
                    print(f'inventory {player.items}')
            elif act == 'examine':
                if selected in player.items:
                    print(item_list[selected].description)
                    print('\n\n')
        else:
            print('')
    else:
        print("\n you aren't carrying anything right now")
direction_dict = {
    'n': '.n_to',
    's': '.s_to',
    'e': '.e_to',
    'w': '.w_to'
}





def travel_to_room(curr_room):
            direction = input('Which direction shall you go?\n')
            if direction in direction_dict:
                return curr_room[direction_dict[direction]][0]
            else: 
                print("please enter n s e or w")
                return curr_room
            # if direction == 'n':
            #     if curr_room.n_to != None:
            #         return curr_room.n_to
            #     else: 
            #         print('THERE IS NOTHING TO THE NORTH\n')
            #     return curr_room
            # elif direction == 'e':
            #     # if hasattr(curr_room, 'e_to'):
            #     if curr_room.e_to != None:
            #         return curr_room.e_to
            #     else: 
            #         print('THERE IS NOTHING TO THE EAST\n')
            #     return curr_room
            # elif direction == 's':
            #     if curr_room.s_to != None:
            #         return curr_room.s_to
            #     else: 
            #         print('THERE IS NOTHING TO THE SOUTH\n') 
            #     return curr_room
            # elif direction == 'w':
            #     if curr_room.w_to != None:
            #         return curr_room.w_to
            #     else: 
            #         print('THERE IS NOTHING TO THE WEST\n')
            #     return curr_room
            # else:
            #     print('PLEASE ENTER either n s e or w TO MOVE OR q TO QUIT\n')
            #     return curr_room
# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items, isLight, naturalLight, correct_item, ius, alt_desc, detail, alt_detail):
        self.name = name
        self.description = description
        self.new_passage = False
        self.items = items
        self.isLight = isLight
        self.naturalLight = naturalLight
        self.n_to=None
        self.e_to=None
        self.s_to=None
        self.w_to=None
        self.correct_item = correct_item
        self.item_use_success = ius
        self.item_use_failure = 'Not sure what you were expecting, but nothing happened.'
        self.alt_desc = alt_desc
        self.detail = detail
        self.alt_detail = alt_detail

    def __str__(self):
        if self.isLight == True or self.naturalLight == True:
            return f"You have entered the {self.name}. {self.description}"
        else:
            return f"It's pitch black!"

    def search_room(self):
        if self.isLight == True or self.naturalLight == True or 'torch' in self.items:
            #if the room contains items
            if len(self.items) > 0:   
                print('You have found:')             
                print(*self.items)
                print('\n')
            else:
                print(f'\nYou found nothing. May as well move on.\n')
        else: 
            print(f'\nGood luck finding anything in the dark...')

    def remove_item(self, item):
        index = self.items.index(item)
        del self.items[index]

    def add_item(self, current_item):
        self.items.append(current_item)

    def illuminate(self):
        self.isLight = True
    
    def darken(self):
        self.isLight = False

    def failure(self):
        print(self.item_use_failure)

    def success(self):
        print(self.item_use_success)
        self.new_passage = True

    def describe(self):
        if self.new_passage == False:
            print(self.detail)
        else: 
            print(self.alt_detail)
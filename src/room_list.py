from room import Room

#name, description, list of items, isLight, naturalLight, the correct item, message on item success, alternate description, details, alternate details
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", ['sword'], True, True, "", "", "", "There's a bush off to the site of the cave entrance. It's cold outside. Better head in.", ""),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", ['torch'], True, True, "", "", "", "Smells like smoke in here.", ""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",[], True, True, "ring", "You toss the ring into the chasm. As it plunges, a the light grows until it fills the room. Lava surges up until it lands on either side of the chasm and quickly cools, forming a new pathway to the north", "A new path is open before you to the north, via lava bridge. The way back is south.", "Lava bubbles ominously below. Hungry, even." , "How did it cool so fast? How can it support your weight? Magic. It's magic lava, ok?"),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",['ring'], False, False, "", "", "", "Scattered remnants of travelers past litter the floor of the passage." , ""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",[], False, False, "hammer", "You spot a suspicious looking brick in the wall. You pound at it until a portion of the wall gives way. Before you lies a new passage to the north.", "You stand in an empty chamber with a hole in the northern wall.", "There's something... not right about the northern wall. Seems fragile." , "You've driven a hammer through the wall. Hope there aren't any curses or anything."),

    'secret': Room("Secret Passage", """The glimmer of light turns out to be two widely-spaced metal hooks mounted to the wall. Curious.""",[], False, False, "sword", "You place the sword gently onto the hooks, bracing yourself for a booby-trap. You are instead greeted with a pleasant 'click' and the eastern wall sliding open.","The room is empty save for a sword hanging on the wall, a crudely made exit to the south, and an opening to the east.", "The hooks look as if something was meant to hang there, in a place of prominence." , "a sword hangs on the wall"),

    'tomb': Room('Tomb', """The light from your torch is reflecting upon a quite substantial pile of gold lying on the floor! """, ['gold'], False, False, "", "", "", "What are you waiting for?? You came for riches!", ""),

    'workroom': Room("Workroom", """Before you lies what appears to be an abandoned work room. A bench with some tools is pushed up against the back wall.""", ['hammer'], False, False, "", "", "", "I bet there's something useful in here if you'd just look around a bit","")
}
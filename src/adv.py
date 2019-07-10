import os
import time
from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "outside",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", "foyer","""Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", "overlook","""A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", "narrow", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber","treasure", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
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

keybindings = {"n":"n_to","s":"s_to","e":"e_to","w":"w_to"}

def draw(position):
    treasure = "*" if position=="treasure"  else " "
    outside = "*" if position=="outside"  else " "
    narrow = "*" if position=="narrow"  else " "
    foyer = "*" if position=="foyer"  else " "
    overlook = "*" if position=="overlook"  else " "

    print("\t\t\t","Overlook","|"," Treasure", "|")
    print("\t\t\t          |           |")
    print(f"\t\t\t     {overlook}    |     {treasure}     |")
    print("\t\t\t          |           |")
    print("\t\t\t-----------------------")
    print("\t\t\t","  Foyer ","|","  Narrow ", "|")
    print("\t\t\t          |           |")
    print(f"\t\t\t     {foyer}    |     {narrow}     |")
    print("\t\t\t          |           |")
    print("\t\t\t-----------------------")
    print("\t\t\t"," Outside","|","         ", "|")
    print("\t\t\t          |           |")
    print(f"\t\t\t     {outside}    |           |")
    print("\t\t\t          |           |")

def welcome():
    print(
"""           _______ _______ ______  ______  _______
    |      |_____| |  |  | |_____] |     \ |_____|
    |_____ |     | |  |  | |_____] |_____/ |     |
    
    _______ ______  _    _ _______ __   _ _______ _     _  ______ _______
    |_____| |     \  \  /  |______ | \  |    |    |     | |_____/ |______
    |     | |_____/   \/   |______ |  \_|    |    |_____| |    \_ |______\n\n\n""")

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

def main():
    os.system('clear')
    player1 = Player()
    welcome()
    while True:
        draw(player1.current_room)
        user_input = input("\n\nWhich direction would you like to move?\t")
        user_input = user_input.strip().lower()
        
        if(user_input=="n" or user_input=="s" or user_input=="e" or user_input=="w"):
            direction = keybindings[user_input]
            next_room = room[player1.current_room].neighbor(direction)
            if(next_room):
                player1.current_room = next_room
                os.system('clear')
                continue
            else:
                print("There is no room available in that direction\n\tor the desired room is not avaible in that direction\n\n")
                input("Hit Return/Enter to continue the game\n\n")
                os.system("clear")
                continue
        elif(user_input=="q"):
            print("Thank You for playing Lamba Adventure")
            time.sleep(.7)
            os.system('clear')
            break
        elif(user_input=="h"):
            print("Available options are:\n\th = List available options\n\tn = move North\n\ts = move South\n\te = move Eest\n\tw = move West")
            input("Hit Return/Enter to continue the game")
            os.system("clear")
            continue
        else:
            print("Input was not recognized")
            print("Available options are:\n\th = List available options\n\tn = move North\n\ts = move South\n\te = move Eest\n\tw = move West")
            input("Hit Return/Enter to continue the game")
            os.system("clear")
            continue

if __name__ == '__main__':
    main()
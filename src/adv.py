import os
import time
from room import Room
from player import Player,Warrior
from item import Item


# Declare all the items
items = {
            "gold":Item(
                "gold",
                "Shiny doubloons used to trade for other items"
            ),
            "sword":Item(
                "sword",
                "A weapon that is used to destroy your enemies"
            ),
            "health_potion":Item(
                "healing potion",
                "An elixer to increase one's health points"
            )
        }

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "outside",
                     "North of you, the cave mount beckons", [items["sword"]] ),

    'foyer':    Room("Foyer", "foyer","""Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", "overlook","""A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [items["health_potion"]]),

    'narrow':   Room("Narrow Passage", "narrow", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber","treasure", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",[items["gold"]]),
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

keybindings = {
    "n":{
        "name":"n_to",
        "description":"Move North"
        },
    "s":{
        "name":"s_to",
        "description":"Move South"
        },
    "e":{
        "name":"e_to",
        "description":"Move East"
        },
    "w":{
        "name":"w_to",
        "description":"Move West"
        },
    "h":{
        "name":"help",
        "description":"List availble options"
        },
    "v":{
        "name":"view",
        "description":"View items in a room"
        },
    "p":{
        "name":"pick",
        "description":"Pick up and item in a room"
        },
    "i":{
        "name":"inventory",
        "description":"View inventory"
        },
    "d":{
        "name":"drop",
        "description":"Drop item from inventory"
        }
}

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


def view_items(items):
    if(len(items) == 0):
        print("\nThis room doesn't have any items\n")
    else:
        [print(f"\n\n\tname: {i.name}\n\tdescription: {i.description}\n\n") for i in items]
    input("Hit Return/Enter to continue the game\n\n")

def print_help():
    print("Available options are:")
    for binding,value in keybindings.items():
        desc = value["description"]
        print(f"\t{binding} = {desc}")
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
        user_input = input("\n\nWhat action would you like to do?\t")
        user_input = user_input.strip().lower()
        
        if(user_input=="n" or user_input=="s" or user_input=="e" or user_input=="w"):
            direction = keybindings[user_input]["name"]
            next_room = room[player1.current_room].neighbor(direction)
            if(next_room):
                if(next_room == "overlook" ):
                    player1 = Warrior.from_human(player1)
                    print(player1.type)
                    print("Congrats, your're a Warrior")
                    input("Hit Return/Enter to continue the game\n\n")
                player1.current_room = next_room
                os.system('clear')
                continue
            else:
                print("There is no room available in that direction\n\tor the desired room is not avaible in that direction\n\n")
                input("Hit Return/Enter to continue the game\n\n")
                os.system("clear")
                continue
        elif(user_input=="q"):
            print("\n\nThank You for playing Lamba Adventure\n\n")
            time.sleep(.7)
            os.system('clear')
            break
        elif(user_input == "v"):
            view_items(room[player1.current_room].list_items())
            os.system('clear')
        elif(user_input == "p"):
            player1.get_item(room[player1.current_room])
            input("\nHit Return/Enter to continue the game")
            os.system('clear')
        elif(user_input == "d"):
            player1.drop_item(room[player1.current_room])
            input("\nHit Return/Enter to continue the game")
            os.system('clear')
        elif(user_input=="h" or user_input=="help"):
            print_help()
            input("\nHit Return/Enter to continue the game")
            os.system("clear")
            continue
        elif(user_input=="i"):
            player1.view_items()
            input("\nHit Return/Enter to continue the game")
            os.system("clear")
            continue
        else:
            print("Input was not recognized")
            print_help()
            input("\nHit Return/Enter to continue the game")
            os.system("clear")
            continue

if __name__ == '__main__':
    main()
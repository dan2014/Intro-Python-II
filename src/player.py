# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self,name="Player 1",current_room="outside"):
        self.name = name
        self.current_room = current_room
        self.items = []

    def get_item(self,room):
        if(len(room.items) == 0):
            print("\nThere are no items to pick up in this room")
        else:
            user_input = input("\nWhat item would like to pick up?\t")
            for x in room.items:
                if(x.name == user_input):
                    requested_item = x
                    room.remove_item(x)
                    self.items.append(x)
                    print(f"\n{requested_item.name} was picked up")
                else:
                    print("\nThat item is not in the room")
    
    def drop_item(self,room):
        if(len(self.items) == 0):
            print("\nThere are no items to drop")
        else:
            user_input = input("\nWhat item would like to drop?\t")
            for i,x in enumerate(self.items):
                if(x.name == user_input):
                    requested_item = x
                    room.add_item(x)
                    self.items.pop(i)
                    print(f"\n{requested_item.name} was dropped up")
                else:
                    print("\nThat item is not in the room")

    def view_items(self):
        if(len(self.items) == 0):
            print("\n\tYou have nothing in your inventory\n")
        else:
            print("\nInventory:")
            [print(f"\n\t{x.name}\n") for x in self.items]

class Warrior(Player):
    def __init__(self,newClass=None):
        if(newClass is None):
            print("if")
            super().__init__()
        else:
            print("else")
            super().__init__(name=newClass.name,current_room=newClass.current_room)
        
        self.type = "Warrior"

    @classmethod
    def from_human(cls,obj):
        return cls(obj)

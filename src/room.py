# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    room_instances = 0

    def __init__(self,name,nickname,description,items=None):
        self.name = name
        self.nickname = nickname
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        if(items==None):
            self.items = []
        else:
            self.items = items

        Room.room_instances +=1

    def neighbor(self,direction):
        next_room = getattr(self,direction)
        if(next_room):
            return next_room.nickname
        else:
            return None

    def list_items(self):
        return self.items
    
    def add_item(self,item):
        return self.items.append(item)

    def remove_item(self,item):
        return self.items.remove(item)
        

    @classmethod
    def room_amount(cls):
        return cls.room_instances

    def __str__(self):
        print(f"Name    {self.name}\nDescription    {self.description}")
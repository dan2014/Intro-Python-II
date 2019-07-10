# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self,name,nickname,description):
        self.name = name
        self.nickname = nickname
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def neighbor(self,direction):
        next_room = getattr(self,direction)
        if(next_room):
            return next_room.nickname
        else:
            return None

    def __str__(self):
        print(f"Name    {self.name}\nDescription    {self.description}")
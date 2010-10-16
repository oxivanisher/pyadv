from room import *
from item import *

class Player(object):
    
    def __init__(self, name, location):
        self.name = name;
        self.location = location;
        
    def go_to_room(self, room):
        self.location = room.get_id();
        
    def get_room(self):
        return self.location;
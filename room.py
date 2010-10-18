from item import *

class Room(object):
    """ This class represents a room. """
    
    def __init__(self, game, id, name):
        self.id = id
        self.name = name;
        self.description = ""
        self.connections = []
        self.game = game
        self.__first_enter = True
        self.inventory = Inventory()
        
    def __str__(self):
        return self.id
    
    def connect(self, room):
        self.connections.append(room)
        room.connections.append(self)
    
    def disconnect(self, room):
        self.connections.remove(room)
        room.connections.remove(self)
    
    def get_id(self):
        return self.id
    
    def set_name(self, name):
        self.name = name
        
    def get_name(self, name):
        return self.name
    
    def set_description(self, description):
        self.description = description
        
    def get_description(self, description):
        return self.description
    
    def get_items(self):
        pass

    def get_connected_rooms(self):
        return self.connections
    
    def enter(self):
        if self.__first_enter:
            self.__first_enter = False
            self.on_first_enter()
        self.on_enter()
        
    def leave(self):
        self.on_leave()
        


    def on_first_enter(self):
        self.game.output_line("You first entered %s" % (self.name))
        
    def on_enter(self):
        self.game.output_line("You enter %s" % (self.name))
    
    def on_leave(self):
        self.game.output_line("You leave %s" % (self.name))
    

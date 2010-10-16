from item import *

class Room(object):
    
    def __init__(self, id, name):
        self.id = id;
        self.name = name;
        self.description = "";
        self.connections = [];
    
    def connect(self, room):
        self.connections.append(room);
        room.connections.append(self.name);
    
    def disconnect(self, room):
        self.connections.remove(room);
        room.connections.remove(self.name);
    
    def get_id(self):
        return self.id;
    
    def set_name(self, name):
        self.name = name;
        
    def get_name(self, name):
        return self.name;
    
    def set_description(self, description):
        self.description = description;
        
    def get_description(self, description):
        return self.description;
    
    def get_items(self):
        pass

    def get_connected_rooms(self):
        return self.connections;
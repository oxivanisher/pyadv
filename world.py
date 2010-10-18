from room import *
from player import *

class World(object):
    
    def __init__(self):
        self.__rooms = [];
        self.rooms_by_id = {};
        self.__player = Player(None)


    def build(self):
        room = self.__add_room(Room("living_room", "Living Room"));
        room.set_description("This is where you live.");
        
        room = self.__add_room(Room("bedroom", "Bedroom"));
        room.set_description("This is where you sleep.");
        
        room = self.__add_room(Room("toilet", "Toilet"));
        room.set_description("This is where you do your private stuff.");
        
        room = self.__add_room(Room("dining_room", "Dining Room"));
        room.set_description("This is where you eat your Meal.");
        
        room = self.__add_room(Room("balcony", "Balcony"));
        room.set_description("This is where you Chill.");

        room = self.__add_room(Room("entrance", "Entrance"));
        room.set_description("This is where you enter the Flat.");

        self.__connect_rooms("living_room", "bedroom");
        self.__connect_rooms("living_room", "dining_room");
        self.__connect_rooms("living_room", "balcony");
        self.__connect_rooms("living_room", "entrance");

        self.__connect_rooms("dining_room", "toilet");
        self.__connect_rooms("dining_room", "balcony");
        
        self.__connect_rooms("bedroom", "toilet");

        self.__player.location = self.get_room_by_id("entrance")
        
    def get_room_by_id(self, id):
        return self.rooms_by_id[id];
  
    def __connect_rooms(self, a, b):
        room_a = self.get_room_by_id(a);
        room_b = self.get_room_by_id(b);
        room_a.connect(room_b);
    
    def __add_room(self, room):
        self.__rooms.append(room);
        self.rooms_by_id[room.get_id()] = room;
        return room;
    
    def __get_rooms(self):
        return self.__rooms
    
    def __get_player(self):
        return self.__player
    
    rooms = property(__get_rooms, None)
    player = property(__get_player, None)
    
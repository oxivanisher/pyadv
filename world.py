from room import *
from player import *
from content import *

class World(object):
    
    def __init__(self, game):
        self.game = game
        self.__rooms = []
        self.__rooms_by_id = {}
        self.__items = []
        self.__items_by_id = {}
        self.__player = Player(game, None)

    def build(self):
        room = self.__add_room(Room(self.game, "living_room", "Living Room"))
        room.set_description("This is where you live.")
        self.__add_item(Item(self.game, "table", "A Table"), room.inventory)
        
        room = self.__add_room(Room(self.game, "bedroom", "Bedroom"))
        room.set_description("This is where you sleep.")
        
        room = self.__add_room(Room(self.game, "toilet", "Toilet"))
        room.set_description("This is where you do your private stuff.")
        
        room = self.__add_room(Room(self.game, "dining_room", "Dining Room"))
        room.set_description("This is where you eat your Meal.")
        
        room = self.__add_room(Room(self.game, "balcony", "Balcony"))
        room.set_description("This is where you Chill.")

        room = self.__add_room(RoomEntrance(self.game, "entrance", "Entrance"))
        room.set_description("This is where you enter the Flat.")
        self.__add_item(Item(self.game, "gun_rack", "A Gun Rack"), room.inventory)

        self.__connect_rooms("living_room", "bedroom")
        self.__connect_rooms("living_room", "dining_room")
        self.__connect_rooms("living_room", "balcony")
        self.__connect_rooms("living_room", "entrance")

        self.__connect_rooms("dining_room", "toilet")
        self.__connect_rooms("dining_room", "balcony")
        
        self.__connect_rooms("bedroom", "toilet")

        self.__add_item(Item(self.game, "pen", "A Pen"), self.player.inventory)
        self.__add_item(Item(self.game, "paper", "A piece of Paper"), self.player.inventory)
        
        
    def get_room_by_id(self, id):
        return self.__rooms_by_id[id]
  
    def __connect_rooms(self, a, b):
        room_a = self.get_room_by_id(a)
        room_b = self.get_room_by_id(b)
        room_a.connect(room_b)
    
    def __add_room(self, room):
        self.__rooms.append(room)
        self.__rooms_by_id[room.get_id()] = room
        return room
    
    def __add_item(self, item, inventory):
        self.__rooms.append(item)
        self.__rooms_by_id[item.get_id()] = item
        inventory.add_item(item)
    
    def get_item_by_id(self, id):
        return self.__items_by_id[id]
    
    def __get_rooms(self):
        return self.__rooms
    
    def __get_player(self):
        return self.__player
    
    rooms = property(__get_rooms, None)
    player = property(__get_player, None)
    
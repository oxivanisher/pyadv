from room import *
from item import *

class Player(object):
        
    def __init__(self, game, location):
        self.game = game
        self.__name = "Nobody"
        self.__location = location
        self.inventory = Inventory()
           
    def __get_name(self):
        return self.__name
        
    def __set_name(self, name):
        self.__name = name
        
    def __get_location(self):
        return self.__location
        
    def __set_location(self, location):
        # leave current room
        if self.__location:
            self.__location.leave()
        # set new location
        self.__location = location
        # enter new location
        self.__location.enter()
 
    name = property(__get_name, __set_name)
    location = property(__get_location, __set_location)
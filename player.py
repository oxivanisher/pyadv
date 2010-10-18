from room import *
from item import *

class Player(object):
        
    def __init__(self, location):
        self.__name = "Nobody"
        self.__location = location
    
    def __del__(self):
        print "Good bye %s" % (self.name)
        
    def __get_name(self):
        return self.__name
        
    def __set_name(self, name):
        self.__name = name
        
    def __get_location(self):
        return self.__location
        
    def __set_location(self, location):
        self.__location = location
 
    name = property(__get_name, __set_name)
    location = property(__get_location, __set_location)
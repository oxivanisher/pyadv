import sys
from room import *
from item import *

class Player(object):
    
    def __init__(self, location):
        self.name = self.__get_name();
        print "Hello %s" % (self.name);
        self.location = location;
    
    def __del__(self):
        print "Good bye %s" % (self.name);
        
    def get_location_id(self):
        return self.location;

    def __get_name(self):
        print "Pleas enter your name: ";
        return sys.stdin.readline();
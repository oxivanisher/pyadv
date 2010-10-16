import sys
from world import *
from player import *

class Navigator (object):
    
    def __init__(self, world):
        self.world = world;
        self.player = Player(world.get_start_room());
        
    
    def run(self):
        
        while (1):
            print "Location: %s" % (self.player.location.name);
            
            for room in self.player.location.get_connected_rooms():
                print "You can go to: %s" % (room.name);
            
            
            input = self.__get_input();
            try:
                num =  int(input);
            except ValueError:
                num = 1000;
            #print "Your entry: %s (%d)" % (input, num);
                
        
        print "Hello World\n"
        
        
    def __get_input(self):
        return sys.stdin.readline();
    

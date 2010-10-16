import sys
from world import *
from player import *

class Navigator (object):
    
    def __init__(self, world):
        self.world = world;
        self.player = Player(world.get_start_room());
    
    def run(self):
        
        navigation = Navigation();
        
        while (1):
            navigation.clear();
            
            print "Location: %s" % (self.player.location.name);
            
            print "Go to: ";
            for room in self.player.location.get_connected_rooms():
                print "[%d]\t%s" % (navigation.add(room), room.name);
                
        
            
            input = self.__get_input();
            try:
                num =  int(input);
            except ValueError:
                num = 1000;
            #print "Your entry: %s (%d)" % (input, num);

            if navigation.exists(num):
                self.player.go_to_room(navigation.get(num));
            else:
                print "Unknown key!";
                
        
    def __get_input(self):
        return sys.stdin.readline();
    

class Navigation (object):
    
    def __init__(self):
        self.nodes = {};
        self.count = 0;
    
    def add(self, content):
        self.count += 1;
        self.nodes[self.count] = content;
        return self.count;
    
    def clear(self):
        self.count = 0;
        self.nodes.clear();
    
    def get(self, key):
        return self.nodes[key];
    
    def exists(self, key):
        if self.nodes.has_key(key):
            return True;
        else:
            return None;
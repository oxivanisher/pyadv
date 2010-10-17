import sys
from world import *
from player import *

class Navigator (object):
    
    def __init__(self, world):
        self.world = world;
        self.player = Player(world.get_start_room());
    
    def run(self):
        
        while (1):
            nav = Navigation();
            
            print "You:\t%s" % (self.player.location.name);
            for room in self.player.location.get_connected_rooms():
                print "[%d]\t%s" % (nav.add(room), room.name);
            print "[99]\tExit";
            
            print "Go to: ";
            input = self.__get_input();
            try:
                num = int(input);
            except ValueError:
                num = 1000;

            if nav.exists(num):
                self.player.location = nav.get(num);
            elif num == 99:
                break;
            else:
                print "Unknown key!";
                
    def __get_input(self):
        return sys.stdin.readline();
    

class Navigation (object):
    
    def __init__(self):
        self.count = 0;
        self.nodes = {};
    
    def add(self, content):
        self.count += 1;
        self.nodes[self.count] = content;
        return self.count;
    
    def get(self, key):
        return self.nodes[key];
    
    def exists(self, key):
        if self.nodes.has_key(key):
            return True;
        else:
            return None;
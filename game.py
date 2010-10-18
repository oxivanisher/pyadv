import sys
from world import *

class Game (object):
  
    def __init__(self):
        self.world = World();
        self.world.build();

        self.player = self.world.player
    
    def input(self):
        return sys.stdin.readline()
    
    def output(self, text):
        print text
        
    def run(self):
        
        self.output("Pleas enter your name: ")
        self.player.name = self.input()
        
        exit_key = 0
        while (1):
            
            self.output("You:\t%s" % (self.player.location.name))
            
            rooms = self.player.location.get_connected_rooms()
            for index, room in enumerate(rooms):
                self.output("[%d]\t%s" % (index + 1, room.name))
            exit_key = index + 2
            self.output("[%d]\tExit" % (exit_key))
            
            self.output("Go to: ")
            input = self.input()
            try:
                num = int(input)
            except ValueError:
                num = 1000
                
            if num >= 1 and num <= len(rooms):
                self.player.location = rooms[num - 1]
            elif num == exit_key:
                break
            else:
                self.output("Unknown key!")
import sys
from world import *


class Navigator (object):
    
    def __init__(self, map):
        self.map = map;
        self.location = map.get_start_room();
    
    def run(self):
        
        while (1):
            input = sys.stdin.readline();
            try:
                num =  int(input);
            except ValueError:
                num = 1000;
            print "Your entry: %s (%d)" % (input, num);
                
        
        print "Hello World\n"
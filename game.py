import sys
from world import *
from content import *

class Game (object):
  
    def __init__(self):
        self.__game_running = True
        self.world = World(self);
        self.world.build();
        self.player = self.world.player
    
    def input(self):
        return sys.stdin.readline()
    
    def output_line(self, text):
        sys.stdout.write(text + "\n")

    def output(self, text):
        sys.stdout.write(text)

    def __game_init(self):
        self.output("Pleas enter your name: ")
        self.player.name = self.input()        
        self.player.location = self.world.get_room_by_id("entrance")

    def __show_menu(self):
        rooms = self.player.location.get_connected_rooms()
        for index, room in enumerate(rooms):
            self.output_line("[%d]\t%s" % (index + 1, room.name))
        for item in self.player.location.inventory.get_items():
            self.output_line("%s (%s)" % (item.name, item.id))
    
    def __process_input(self, text):
        args = text.lower().strip().split(' ')
        cmd = args[0]
        args = args[1:]
        
        cmds = {
            'go' : self.__command_go,
            'get' : self.__command_get,
            'put' : self.__command_put,
            'use' : self.__command_use,
            'talk' : self.__command_talk,
            'inventory' : self.__command_inventory,
            'exit' : self.__command_exit,
        }
        
        try:
            cmds[cmd](args)
        except KeyError:
            self.output("Unknown command. Available: ")
            for key in cmds.keys():
                self.output(key + " ")
            self.output_line("")
 
    def __enter_room(self, num):           
        rooms = self.player.location.get_connected_rooms()
        if num >= 1 and num <= len(rooms):
            self.player.location = rooms[num - 1]
        else:
            self.output_line("Unknown room!")
    
    def __command_go(self, args):
        try:
            num = int(args[0])
        except IndexError, ValueError:
            num = 1000
        self.__enter_room(num)
    
    def __command_get(self, args):
        pass

    def __command_put(self, args):
        pass
    
    def __command_use(self, args):
        pass
    
    def __command_talk(self, args):
        pass
 
    def __command_inventory(self, args):
        for item in self.player.inventory.get_items():
            self.output_line("%s (%s)" % (item.name, item.id))
    
    def __command_exit(self, args):
        self.__game_running = False
    
    def run(self):
        
        self.__game_init()

        self.__game_running = True
        while (self.__game_running):
            self.__show_menu()
            self.output(": ")
            self.__process_input(self.input())
        
        self.output("Good bye %s" % (self.player.name))

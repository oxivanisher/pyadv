from room import *

class RoomEntrance(Room):
    def on_enter(self):
        self.game.output_line("Aloha")
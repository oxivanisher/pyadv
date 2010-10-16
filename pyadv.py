from navigator import *
from world import *

def main():
    world = World();
    world.build();
    navigator = Navigator(world);
    navigator.run();
    
    
main();
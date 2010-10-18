class Item(object):
    """ This class represents a item. """
    
    def __init__(self, game, id, name):
        self.game = game
        self.id = id
        self.name = name
        self.description = ""
        self.fixed = True
        self.__inventory = None
        
    def __str__(self):
        return self.id

    def get_id(self):
        return self.id
    
    def set_name(self, name):
        self.name = name
        
    def get_name(self, name):
        return self.name
    
    def set_description(self, description):
        self.description = description
        
    def get_description(self, description):
        return self.description
    
    def __get_inventory(self):
        return self.__inventory
    
    def __set_inventory(self, inventory):
        self.__inventory = inventory
    
    inventory = property(__get_inventory, __set_inventory)

class Inventory(object):
    
    def __init__(self):
        self.__items = []
        
    def add_item(self, item):
        if item.inventory:
            item.inventory.__items.remove(item)
        self.__items.append(item)
            
    def get_items(self):
        return self.__items
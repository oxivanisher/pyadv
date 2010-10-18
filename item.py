class Item(object):
    """ This class represents a item. """
    
    def __init__(self, id, name, location):
        self.id = id
        self.name = name
        self.description = ""
        self.fixed = True
        self.location = location
        self.inventory = None
        
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

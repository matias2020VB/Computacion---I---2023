class PokemonUser():
    def __init__(self, name, types, moves, EVs, health):
        self.name = name
        self.types = types
        self.moves = moves 
        self.evs = EVs
        self.health = health
    
    def set_name(self, name):
        self.name = name
    
    def set_types(self, types):
        self.types = types
    
    def set_moves(self, moves):
        self.moves = moves
    
    def set_evs(self, evs):
        self.evs = evs
        
    def set_health(self, health):
        self.health = health
    
    def get_name(self):
        return self.name
    
    def get_types(self):
        return self.types
    
    def get_moves(self):
        return self.moves
    
    def get_evs(self):
        return self.evs
    
    def get_health(self):
        return self.health
    
    
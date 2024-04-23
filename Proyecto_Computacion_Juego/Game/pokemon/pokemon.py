# Clase Pokemon que contiene los atributos y metodos de los pokemones.

class Pokemon:
    def __init__(self, name, types, moves, EVs, health= 100):
        self.name = name
        self.types = types
        self.moves = moves + ['Huir'] + ['Usar poción']
        self.attack = EVs['ATTACK']
        self.defense = EVs['DEFENSE']
        self.health = health
        self.level = 1
        self.dead = False
        self.exp = 0
        self.exp_next_level = 50
    
    def set_name(self, name):
        self.name = name
    
    def set_types(self, types):
        self.types = types
    
    def set_moves(self, moves):
        self.moves = moves
    
    def set_attack(self, attack):
        self.attack = attack
    
    def set_defense(self, defense):
        self.defense = defense
    
    def set_health(self, health):
        self.health = health
    
    def set_level(self, level):
        self.level = level
    
    def set_dead(self, dead):
        self.dead = dead
    
    def set_exp(self, exp):
        self.exp = exp
        
    def set_exp_next_level(self, exp_next_level):
        self.exp_next_level = exp_next_level
    
    def get_name(self):
        return self.name
    
    def get_types(self):
        return self.types
    
    def get_moves(self):
        return self.moves
    
    def get_attack(self):
        return self.attack
    
    def get_defense(self):
        return self.defense
    
    def get_health(self):
        return self.health
    
    def get_level(self):
        return self.level
    
    def get_dead(self):
        return self.dead
    
    def get_exp(self):
        return self.exp
    
    def get_exp_next_level(self):
        return self.exp_next_level
    
import time
import numpy as np
import sys

# Delay printing

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

# Creamos clase Pokemon

class Pokemon:
    def __init__(self, name,  types, moves, EVs, health='==================='):
        
        # Guardar cualquier variable como atributo para cada objeto Pokemón.
        
        self.name = name
        self.types = types
        self.moves = moves
        self.attack = EVs['ATTACK']
        self.defense = EVs['DEFENSE']
        self.health = health
        self.bars = 15  # Cantidad de barras de salud que quedan para cada pokemon


    def fight(self, Pokemon2):
        
        # Permitir a dos pokemon luchar entre sí
        
        # Muestreo de la informacion de pelea.
        
        print("-----POKEMON BATTLE-----")
        print(f"\n{self.name}")
        print("TYPE/", self.types)
        print("ATTACK/", self.attack)
        print("DEFENSE/", self.defense)
        print("LVL/", 3*(1+np.mean([self.attack,self.defense]))) 

# Calculamos su nivel en funcion de su ataque y defensa, haremos el promedio entre ambos y lo multiplicaremos por 3 para obtener el nivel.
        
        print("\nVS")
        
        print(f"\n{Pokemon2.name}")
        print("TYPE/", Pokemon2.types)
        print("ATTACK/", Pokemon2.attack)
        print("DEFENSE/", Pokemon2.defense)
        print("LVL/", 3*(1+np.mean([Pokemon2.attack,Pokemon2.defense])))
        
        
        time.sleep(2)
        
        # Ventajas considerando el tipo de pokemon.
        
        version = ['Fire', 'Water', 'Grass']
        
        # Iteramos sobre cada elemento de la lista version. Donde "i" es el indice y "k" es el valor actual de la lista. 
        
        for i,k in enumerate(version):
            if self.types == k:
                
                # Ambos son del mismo tipo
                if Pokemon2.types == k:
                    string_1_attack = '\nNo ha sido muy efectivo.. intenta nuevamente.'
                    string_2_attack = '\nNo ha sido muy efectivo.. intenta nuevamente.'
                
                # Pokemon2 es del tipo Grass
                if Pokemon2.types == version[(i+1)%3]:
                    Pokemon2.attack *= 2
                    Pokemon2.defense *= 2
                    self.attack /= 2
                    self.defense /= 2
                    string_1_attack = '\nNo ha sido muy efectivo.. intenta nuevamente.'
                    string_2_attack = '\nHa sido muy efectivo!, genial!'
                
                # Pokemon2 es del tipo Water
                if Pokemon2.types == version[(i+2)%3]:
                    self.attack *= 2
                    self.defense *= 2
                    Pokemon2.attack /= 2
                    Pokemon2.defense /= 2
                    string_1_attack = '\nHa sido muy efectivo!, genial!'
                    string_2_attack = '\nNo ha sido muy efectivo.. intenta nuevamente.'
        self.health = ""
        
        # Ahora para la pelea real.
        
        # Mientras que el pokemon 1 y el pokemon 2 tengan barras de salud, la pelea continua. 
        
        while (self.bars > 0) and (Pokemon2.bars > 0):
            
            # Imprimimos la salud de cada pokemon.
            
            print(f"\n{self.name}\t\tHLTH\t{self.health}")
            
            print(f"{Pokemon2.name}\t\tHLTH\t{Pokemon2.health}\n")
            
            # Turno del Pokemon1
            
            print(f"Go {self.name}!")
            
            for i, x in enumerate(self.moves):
                print(f"{i+1}.", x)
            
            index = int(input('Pick a move: '))
            
            delay_print(f"\n{self.name} used {self.moves[index-1]}!")
            
            time.sleep(1)
            
            delay_print(string_1_attack)
            
            # Determinamos el daño.
            
            Pokemon2.bars -= self.attack
            
            Pokemon2.health = ""
            
            # Plus de defensa
            
            for j in range(int(Pokemon2.bars+0.1*Pokemon2.defense)):
                Pokemon2.health += "="
            
            time.sleep(1)
            print(f"\n{self.name}\t\tHLTH\t{self.health}")
            print(f"{Pokemon2.name}\t\tHLTH\t{Pokemon2.health}\n")
            time.sleep(.5)
            
            # Checkeamos si el pokemon esta fatigado. Si es asi, termina la pelea.
            
            if Pokemon2.bars <= 0:
                delay_print("\n..." + Pokemon2.name + ' fainted.')
                break
            
            # Turno del Pokemon2
            
            print(f"Go {Pokemon2.name}!")
            
            for i, x in enumerate(Pokemon2.moves):
            
                print(f"{i+1}.", x)
            
            index = int(input('Pick a move please: '))
            
            delay_print(f"\n{Pokemon2.name} used {Pokemon2.moves[index-1]}!")
            
            time.sleep(1)
            
            delay_print(string_2_attack)
            
            # Determinamos el daño del pokemon 2 hacia el pokemon 1
            
            Pokemon2.bars -= Pokemon2.attack
            
            Pokemon2.health = ""
            
            # Plus de defensa
            
            for j in range(int(self.bars+0.1*self.defense)):
                self.health += "="
            
            time.sleep(1)
            
            print(f"\n{self.name}\t\tHLTH\t{self.health}")
            
            print(f"{Pokemon2.name}\t\tHLTH\t{Pokemon2.health}\n")
            
            time.sleep(.5)
            
            # Checkeamos si el pokemon esta fatigado. Si es asi, termina la pelea.
            
            if self.bars <= 0:
                
                delay_print("\n..." + self.name + ' fainted.')
                
                break
        
        # Cuando finaliza la batalla se le otorga al entrenador una cantidad de dinero aleatoria.
        
        money = np.random.choice(5000)
        delay_print(f"\nOpponent paid you ${money}.\n")

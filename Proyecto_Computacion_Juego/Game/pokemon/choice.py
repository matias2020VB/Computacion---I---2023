from pokemon import PokemonPc
from pokemon import PokemonUser
import constants
import random

# Listas que van a contener los objetos de los pokémon del usuario y de la PC.

user_pokemon = []
pc_pokemon = []

# funcion que permite elegir el pokemon de la PC y guardarlo en una lista.

def choice_pc():
    
# Seleccionar un Pokémon aleatorio de la PC
    
    random_pc_pokemon = random.choice(constants.pc_pokemon)

# Asignar los datos del Pokémon seleccionado a las variables correspondientes
    
    name = random_pc_pokemon['name']
    types = random_pc_pokemon['types']
    moves = random_pc_pokemon['moves']
    EVs = random_pc_pokemon['EVs']
    health = random_pc_pokemon['health']

# Crear un objeto PokemonPc con los datos del Pokémon seleccionado
    
    value = PokemonPc(name, types, moves, EVs, health)
    pc_pokemon.append(value)
    
    # Añade un mensaje para confirmar la inicialización del enemigo
    
    print(f"\nName: {name}\n Types: {types}\n Moves: {', '.join(moves)}\n EVs: {EVs}\n Health: {health}\n")
    input("Pulsa cualquier tecla para volver al menu...")

# Funcion para elegir el pokemon del usuario y guardarlo en una lista.

def choice_user(name):
    for pokemon in constants.user_pokemon:
        if pokemon['name'] == name:
            
            # Asignar los datos del Pokémon seleccionado a las variables correspondientes
            
            name = pokemon['name']
            types = pokemon['types']
            moves = pokemon['moves']
            EVs = pokemon['EVs']
            health = pokemon['health']

            # Crear un objeto PokemonUser con los datos del Pokémon seleccionado.
            
            value = PokemonUser(name, types, moves, EVs, health)
            user_pokemon.append(value)
            
            # Añade un mensaje para confirmar la selección del Pokémon
            
            print(f"\nName: {name}\n Types: {types}\n Moves: {', '.join(moves)}\n EVs: {EVs}\n Health: {health}\n")
            input("Pulsa cualquier tecla para volver al menu...")

            return

    # Si no se encuentra el Pokémon, imprimir un mensaje de error
    print(f"Error: No se encontró un Pokémon con el nombre {name}")
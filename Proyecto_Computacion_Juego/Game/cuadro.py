from tabulate import tabulate
import constants

# Funcion donde se muestra el cuadro de los pokemones.

def mostrar_pokemon_en_cuadro(pokemon_list):
    
    # Tabla que contiene los datos de cada Pokémon / Headers: Encabezado de la tabla
    
    headers = ["Nombre", "Tipo", "Movimientos", "EVs", "Salud"]
    
    # Lista que contiene los datos de cada Pokémon
    
    tabla = []

    # Iterar sobre la lista pokémon
    for pokemon in pokemon_list:
        nombre = pokemon['name']
        tipo = pokemon['types']
        movimientos = ', '.join(pokemon['moves'])
        EVs = ', '.join([f"{key}: {value}" for key, value in pokemon['EVs'].items()])
        salud = pokemon['health']
        tabla.append([nombre, tipo, movimientos, EVs, salud])
    
    # Utilizo la libreria tabulate para mostrar los datos de los pokemones en una tabla. Donde tablefmt="fancy_grid" es el formato de la tabla.
    
    print(tabulate(tabla, headers, tablefmt="fancy_grid"))

# Lista que contiene los datos de los pokemones que son agregados a la tabla.
pokemon_list = [
    {'name': 'Charizard', 'types': 'Fire', 'moves': ['Flamethrower', 'Fly', 'Blast Burn', 'Fire Punch'], 'EVs': {'ATTACK':12, 'DEFENSE':8}, 'health': 100},
    {'name': 'Blastoise', 'types': 'Water', 'moves': ['Water Gun', 'Bubblebeam', 'Hydro Pump', 'Surf'], 'EVs': {'ATTACK':10, 'DEFENSE':10}, 'health': 100},
    {'name': 'Venusaur', 'types': 'Grass', 'moves': ['Vine Wip', 'Razor Leaf', 'Earthquake', 'Frenzy Plant'], 'EVs': {'ATTACK':8, 'DEFENSE':12}, 'health': 100},
    {'name': 'Charmander', 'types': 'Fire', 'moves': ['Ember', 'Scratch', 'Tackle', 'Fire Punch'], 'EVs': {'ATTACK':4, 'DEFENSE':2}, 'health': 100},
    {'name': 'Squirtle', 'types': 'Water', 'moves': ['Bubblebeam', 'Tackle', 'Headbutt', 'Surf'], 'EVs': {'ATTACK':3, 'DEFENSE':3}, 'health': 100},
    {'name': 'Bulbasaur', 'types': 'Grass', 'moves': ['Vine Wip', 'Razor Leaf', 'Tackle', 'Leech Seed'], 'EVs': {'ATTACK':2, 'DEFENSE':4}, 'health': 100},
    {'name': 'Charmeleon', 'types': 'Fire', 'moves': ['Ember', 'Scratch', 'Flamethrower', 'Fire Punch'], 'EVs': {'ATTACK':5, 'DEFENSE':4}, 'health': 100},
    {'name': 'Wartotle', 'types': 'Water', 'moves': ['Bubblebeam', 'Water Gun', 'Headbutt', 'Surf'], 'EVs': {'ATTACK':11, 'DEFENSE':9}, 'health': 100},
    {'name': 'Ivysaur', 'types': 'Grass', 'moves': ['Vine Wip', 'Razor Leaf', 'Bullet Seed', 'Leech Seed'], 'EVs': {'ATTACK':3, 'DEFENSE':5}, 'health': 100}
]

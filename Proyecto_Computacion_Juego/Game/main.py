from pokemon import pokemon_pc
from pokemon import choice
from pokemon_battle import battle_pc
import constants
import cuadro

def start_menu():
    # Variables globales para poder acceder a los datos de los pokemones.
    
    global user_pokemon
    global pc_pokemon
    
    while True:
            print("<<<<<GAME SYSTEM COMBAT>>>>>")
            print("1 = Choice Pokemon:")
            print("2 = Initialize Enemy random:")
            print("3 = Show Pokemon PC:")
            print("4 = Show Pokemon User:")
            print("5 = Initiate Combat:")
            print("6 = <<Exit for videogame>>")
            selection = input("\nCHOOSE THE MODE TO START PLAYING[1/2/3/4/5/6]  = ")

            # Esta opcion del menu permite elegir un pokemon para el usuario.
            if selection == '1':

                cuadro.mostrar_pokemon_en_cuadro(cuadro.pokemon_list)
                pokemon_eleccion = input("Ingresa el nombre del Pokémon que deseas elegir: ")
                user_pokemon = choice.choice_user(pokemon_eleccion)

            # Esta opcion del menu permite elegir un pokemon para la PC.
            
            elif selection == '2':
                
            # Aqui se inicializa el pokemon de la PC random.
                
                pc_pokemon = choice.choice_pc()

            # Esta opcion del menu permite mostrar el pokemon de la PC.
            
            elif selection == "3":
                
                print("\nEl pokemon que salio aleatorio como enemigo es:")
                for pokemon in choice.pc_pokemon:
                    name = pokemon.get_name()
                    types = pokemon.get_types()
                    moves = pokemon.get_moves()
                    EVs = pokemon.get_evs()
                    health = pokemon.get_health()
                    print(f"\nName: {name}\n Types: {types}\n Moves: {', '.join(moves)}\n EVs: {EVs}\n Health: {health}\n")
                    input("Pulsa cualquier tecla para volver al menu por favor..")
            
            
            # Aqui se muestra el pokemon del usuario.
            
            elif selection == "4":
                
                print("\nEl pokemon que elegiste es: ")
                for pokemon in choice.user_pokemon:
                    name = pokemon.get_name()
                    types = pokemon.get_types()
                    moves = pokemon.get_moves()
                    EVs = pokemon.get_evs()
                    health = pokemon.get_health()
                    print(f"\nName: {name}\n Types: {types}\n Moves: {', '.join(moves)}\n EVs: {EVs}\n Health: {health}\n")
                    input("Pulsa cualquier tecla para volver al menu por favor..")

            # Esta opcion del menu permite iniciar el combate entre el pokemon del usuario y el de la PC.
            
            elif selection == "5":
                
                # Aqui se inicializa el pokemon del usuario y el de la PC para la batalla.
                
                for pokemon_data in choice.user_pokemon:
                
                # Aqui se recorre el pokemon elegido por el usuario con las opciones anteriores.
                    
                    user_pokemon_instance = battle_pc.Pokemon(
                        pokemon_data.get_name(),
                        pokemon_data.get_types(),
                        pokemon_data.get_moves(),
                        pokemon_data.get_evs(),
                        pokemon_data.get_health()
                    )
                # Aqui se recorre el pokemon elegido por la PC con las opciones anteriores.
                
                for pokemon_data in choice.pc_pokemon:
                    pc_pokemon_instance = battle_pc.Pokemon(
                        pokemon_data.get_name(),
                        pokemon_data.get_types(),
                        pokemon_data.get_moves(),
                        pokemon_data.get_evs(),
                        pokemon_data.get_health()
                    )
                
                # Aqui se inicia la batalla entre el pokemon del usuario y el de la PC.
                
                user_pokemon_instance.fight(pc_pokemon_instance)

                print("Please choose your Pokemon and initialize the enemy first.")
            
            # Esta opcion del menu permite salir del Juego.
            
            elif selection == '6':

                print("¡Gracias por pelear, espero que vuelvas pronto! :)")
                break

            else:
            
            # Esta opcion del menu permite mostrar un mensaje de error si la opcion no existe en el juego.
                print("\n Esta opción no existe en el videojuego... Elije otra opcion del menu.\n")

start_menu()
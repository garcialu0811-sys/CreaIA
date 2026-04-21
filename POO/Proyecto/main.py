import random
from pokedex import CATALOGO_POKEMON, mostrar_catalogo_disponible
from pokemon_clases import PokemonAgua, PokemonFuego, PokemonPlanta, PokemonElectrico

def seleccionar_pokemon(mensaje):
    """
    Maneja la lógica de selección de Pokémon con validación de errores (Try/Except).
    Cumple con el requerimiento de instanciación dinámica.
    """
    while True:
        mostrar_catalogo_disponible()
        try:
            opcion = input(mensaje)
            if opcion not in CATALOGO_POKEMON:
                print("Error: Selección fuera de rango. Intente de nuevo.")
                continue
            
            # Extracción de datos crudos del catálogo
            datos = CATALOGO_POKEMON[opcion]
            tipo = datos["tipo"]
            nombre = datos["nombre"]
            hp = datos["hp_maximo"]
            ep = datos["energia_maxima"]

            # Instanciación dinámica según el tipo (Polimorfismo/Herencia)
            if tipo == "Fuego":
                return PokemonFuego(nombre, hp, ep)
            elif tipo == "Agua":
                return PokemonAgua(nombre, hp, ep)
            elif tipo == "Planta":
                return PokemonPlanta(nombre, hp, ep)
            elif tipo == "Electrico":
                return PokemonElectrico(nombre, hp, ep)
                
        except ValueError:
            print("Error: Ingrese un número válido.")

def ejecutar_turno(jugador, oponente, es_bot=False):
    """
    Ejecuta la lógica de un turno, ya sea para humano o computadora (PvE).
    """
    print(f"\n--- TURNO DE {jugador.nombre.upper()} ---")
    print(jugador) # Usa el método __str__ definido en tu clase base

    if es_bot:
        # Lógica para la computadora usando random
        accion = random.randint(1, 3)
        print(f"La computadora elige: {accion}")
    else:
        while True:
            try:
                print("1. Atacar (15 EP)\n2. Defender (5 EP)\n3. Descansar (+20 EP)")
                accion = int(input("> Opción: "))
                if accion in [1, 2, 3]: break
                print("Opción no válida.")
            except ValueError:
                print("Error: Ingrese un número (1, 2 o 3).")

    # Procesamiento de la acción seleccionada
    if accion == 1:
        mensaje, _ = jugador.atacar(oponente)
        print(mensaje)
    elif accion == 2:
        print(jugador.defender())
    elif accion == 3:
        print(jugador.descansar())

def main():
    print("="*40)
    print("  SIMULADOR DE BATALLAS POKÉMON (POO)")
    print("="*40)

    # 1. Selección de Modo de Juego
    modo = ""
    while modo not in ["1", "2"]:
        print("1. Jugador vs Jugador (PvP)")
        print("2. Jugador vs Computadora (PvE)")
        modo = input("> Opción: ")

    # 2. Selección de Combatientes
    p1 = seleccionar_pokemon("Jugador 1, elija el número de su Pokémon: ")
    
    if modo == "2":
        print("Computadora eligiendo combatiente...")
        id_bot = str(random.randint(1, len(CATALOGO_POKEMON)))
        # Reutilizamos la lógica de instanciación para el bot
        datos_bot = CATALOGO_POKEMON[id_bot]
        if datos_bot["tipo"] == "Fuego": p2 = PokemonFuego(datos_bot["nombre"], datos_bot["hp_maximo"], datos_bot["energia_maxima"])
        elif datos_bot["tipo"] == "Agua": p2 = PokemonAgua(datos_bot["nombre"], datos_bot["hp_maximo"], datos_bot["energia_maxima"])
        elif datos_bot["tipo"] == "Planta": p2 = PokemonPlanta(datos_bot["nombre"], datos_bot["hp_maximo"], datos_bot["energia_maxima"])
        else: p2 = PokemonElectrico(datos_bot["nombre"], datos_bot["hp_maximo"], datos_bot["energia_maxima"])
    else:
        p2 = seleccionar_pokemon("Jugador 2, elija el número de su Pokémon: ")

    print(f"\n¡COMIENZA LA BATALLA: {p1.nombre} vs {p2.nombre}!")

    # 3. Ciclo Principal de Combate
    turno_actual = 1
    while p1.esta_vivo() and p2.esta_vivo():
        if turno_actual % 2 != 0:
            ejecutar_turno(p1, p2)
        else:
            ejecutar_turno(p2, p1, es_bot=(modo == "2"))
        
        turno_actual += 1

    # 4. Resultado Final
    print("\n" + "X"*30)
    if p1.esta_vivo():
        print(f"¡EL GANADOR ES {p1.nombre.upper()}!")
    else:
        print(f"¡EL GANADOR ES {p2.nombre.upper()}!")
    print("X"*30)

if __name__ == "__main__":
    main()
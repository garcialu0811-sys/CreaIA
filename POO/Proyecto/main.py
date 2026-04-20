
import sys
import random
from pokemon_clases import PokemonAgua, PokemonFuego, PokemonPlanta, PokemonElectrico
from pokedex import CATALOGO_POKEMON, mostrar_catalogo_disponible


def limpiar_pantalla():
    """Limpia la consola para mejorar la experiencia de usuario."""
    print("\n" * 2)


def obtener_entero_valido(mensaje: str, min_val: int, max_val: int) -> int:
    """
    Solicita al usuario un número entero dentro de un rango.
    Maneja errores de entrada (ValueError) y valores fuera de rango.
    """
    while True:
        try:
            entrada = input(mensaje)
            valor = int(entrada)
            if min_val <= valor <= max_val:
                return valor
            else:
                print(f"Error: Ingrese un número entre {min_val} y {max_val}.")
        except ValueError:
            print("Error: Debe ingresar un número válido.")


def seleccionar_pokemon(jugador_nombre: str) -> object:
    """
    Muestra el catálogo y permite al jugador seleccionar un Pokémon.
    Retorna una instancia de la clase hija correspondiente.
    """
    mostrar_catalogo_disponible()
    print(f"{jugador_nombre}, elija el número de su Pokémon:")
    
    opcion = obtener_entero_valido("> Opción: ", 1, len(CATALOGO_POKEMON))
    opcion_str = str(opcion)
    
    datos = CATALOGO_POKEMON[opcion_str]
    tipo = datos["tipo"]
    nombre = datos["nombre"]
    hp_max = datos["hp_maximo"]
    ep_max = datos["energia_maxima"]
    
    # Instanciación dinámica según el tipo
    if tipo == "Agua":
        pokemon = PokemonAgua(nombre, hp_max, ep_max)
    elif tipo == "Fuego":
        pokemon = PokemonFuego(nombre, hp_max, ep_max)
    elif tipo == "Planta":
        pokemon = PokemonPlanta(nombre, hp_max, ep_max)
    elif tipo == "Electrico":
        pokemon = PokemonElectrico(nombre, hp_max, ep_max)
    else:
        raise ValueError(f"Tipo desconocido: {tipo}")
    
    print(f"\n¡Has seleccionado a {nombre}!\n")
    return pokemon


def seleccion_pc() -> object:
    """
    La computadora selecciona un Pokémon aleatorio del catálogo.
    """
    claves = list(CATALOGO_POKEMON.keys())
    opcion_str = random.choice(claves)
    datos = CATALOGO_POKEMON[opcion_str]
    tipo = datos["tipo"]
    nombre = datos["nombre"]
    hp_max = datos["hp_maximo"]
    ep_max = datos["energia_maxima"]
    
    if tipo == "Agua":
        pokemon = PokemonAgua(nombre, hp_max, ep_max)
    elif tipo == "Fuego":
        pokemon = PokemonFuego(nombre, hp_max, ep_max)
    elif tipo == "Planta":
        pokemon = PokemonPlanta(nombre, hp_max, ep_max)
    elif tipo == "Electrico":
        pokemon = PokemonElectrico(nombre, hp_max, ep_max)
    else:
        raise ValueError(f"Tipo desconocido: {tipo}")
    
    print(f"¡La computadora ha seleccionado a {nombre}!\n")
    return pokemon


def accion_pc(pokemon_pc: object) -> int:
    """
    La computadora elige una acción aleatoria: 1 (Atacar), 2 (Defender), 3 (Descansar)
    """
    return random.randint(1, 3)


def mostrar_estado(pokemon1: object, pokemon2: object):
    """Muestra el estado actual de ambos Pokémon en batalla."""
    print("\n" + "-" * 50)
    print(f"{pokemon1}")
    print(f"{pokemon2}")
    print("-" * 50)


def turno_jugador(jugador: object, oponente: object) -> bool:
    """
    Maneja el turno del jugador humano.
    Retorna True si la batalla debe continuar, False si terminó.
    """
    while True:
        print(f"\nTURNO DE {jugador.nombre.upper()}")
        print(f"[HP: {jugador.hp_actual}/{jugador.hp_maximo}] | [EP: {jugador.energia_actual}/{jugador.energia_maxima}]")
        print("\n¿Qué acción deseas realizar?")
        print("1. Atacar (Costo: 15 EP)")
        print("2. Defender (Costo: 5 EP)")
        print("3. Descansar (Restaura: 20 EP)")
        
        accion = obtener_entero_valido("> Opción: ", 1, 3)
        
        if accion == 1:
            mensaje, _ = jugador.atacar(oponente)
            print(f"\n{mensaje}")
            break
        elif accion == 2:
            mensaje = jugador.defender()
            print(f"\n{mensaje}")
            break
        elif accion == 3:
            mensaje = jugador.descansar()
            print(f"\n{mensaje}")
            break
    
    # Verificar si el oponente fue derrotado
    return oponente.esta_vivo()


def turno_pc(jugador: object, oponente: object) -> bool:
    """
    Maneja el turno de la computadora (PvE).
    Retorna True si la batalla debe continuar, False si terminó.
    """
    # Verificar si el oponente está paralizado
    if hasattr(oponente, 'paralizado') and oponente.paralizado:
        print(f"\nTURNO DE {oponente.nombre.upper()} (Computadora)")
        print(f"{oponente.nombre} está paralizado y no puede moverse en este turno!")
        delattr(oponente, 'paralizado')  # La parálisis se consume
        return jugador.esta_vivo()
    
    accion = accion_pc(oponente)
    
    print(f"\nTURNO DE {oponente.nombre.upper()} (Computadora)")
    print(f"[HP: {oponente.hp_actual}/{oponente.hp_maximo}] | [EP: {oponente.energia_actual}/{oponente.energia_maxima}]")
    
    if accion == 1:
        mensaje, _ = oponente.atacar(jugador)
        print(f"\nLa computadora elige: 1 (Atacar)")
        print(mensaje)
    elif accion == 2:
        mensaje = oponente.defender()
        print(f"\nLa computadora elige: 2 (Defender)")
        print(mensaje)
    elif accion == 3:
        mensaje = oponente.descansar()
        print(f"\nLa computadora elige: 3 (Descansar)")
        print(mensaje)
    
    return jugador.esta_vivo()


def turno_pvp(jugador1: object, jugador2: object, jugador_actual: int) -> tuple[bool, int]:
    """
    Maneja un turno en modo PvP.
    Retorna (continuar, siguiente_jugador)
    """
    jugador = jugador1 if jugador_actual == 1 else jugador2
    oponente = jugador2 if jugador_actual == 1 else jugador1
    
    # Verificar parálisis
    if hasattr(jugador, 'paralizado') and jugador.paralizado:
        print(f"\nTURNO DE {jugador.nombre.upper()}")
        print(f"{jugador.nombre} está paralizado y no puede moverse en este turno!")
        delattr(jugador, 'paralizado')
        return (oponente.esta_vivo() and jugador.esta_vivo(), 3 - jugador_actual)
    
    mostrar_estado(jugador, oponente)
    
    print(f"\nTURNO DE {jugador.nombre.upper()}")
    print(f"[HP: {jugador.hp_actual}/{jugador.hp_maximo}] | [EP: {jugador.energia_actual}/{jugador.energia_maxima}]")
    print("\n¿Qué acción deseas realizar?")
    print("1. Atacar (Costo: 15 EP)")
    print("2. Defender (Costo: 5 EP)")
    print("3. Descansar (Restaura: 20 EP)")
    
    accion = obtener_entero_valido("> Opción: ", 1, 3)
    
    if accion == 1:
        mensaje, _ = jugador.atacar(oponente)
        print(f"\n{mensaje}")
    elif accion == 2:
        mensaje = jugador.defender()
        print(f"\n{mensaje}")
    elif accion == 3:
        mensaje = jugador.descansar()
        print(f"\n{mensaje}")
    
    continuar = oponente.esta_vivo() and jugador.esta_vivo()
    return (continuar, 3 - jugador_actual)


def batalla_pve(pokemon_jugador: object, pokemon_pc: object):
    """
    Ejecuta la batalla en modo Jugador vs Computadora.
    """
    print("\n" + "=" * 50)
    print("¡COMIENZA LA BATALLA!")
    print(f"{pokemon_jugador.nombre} ({pokemon_jugador.tipo}) vs {pokemon_pc.nombre} ({pokemon_pc.tipo})")
    print("=" * 50)
    
    turno = 0  # 0 = jugador, 1 = computadora
    
    while True:
        mostrar_estado(pokemon_jugador, pokemon_pc)
        
        if turno == 0:
            # Turno del jugador
            if not turno_jugador(pokemon_jugador, pokemon_pc):
                print(f"\n¡{pokemon_pc.nombre} se ha debilitado! ¡{pokemon_jugador.nombre} gana la batalla!")
                break
            turno = 1
        else:
            # Turno de la computadora
            if not turno_pc(pokemon_jugador, pokemon_pc):
                print(f"\n¡{pokemon_jugador.nombre} se ha debilitado! ¡{pokemon_pc.nombre} gana la batalla!")
                break
            turno = 0


def batalla_pvp(pokemon_j1: object, pokemon_j2: object):
    """
    Ejecuta la batalla en modo Jugador vs Jugador.
    """
    print("\n" + "=" * 50)
    print("¡COMIENZA LA BATALLA!")
    print(f"{pokemon_j1.nombre} ({pokemon_j1.tipo}) vs {pokemon_j2.nombre} ({pokemon_j2.tipo})")
    print("=" * 50)
    
    jugador_actual = 1
    
    while True:
        continuar, jugador_actual = turno_pvp(pokemon_j1, pokemon_j2, jugador_actual)
        if not continuar:
            break
    
    # Determinar ganador
    if not pokemon_j1.esta_vivo():
        print(f"\n¡{pokemon_j1.nombre} se ha debilitado! ¡{pokemon_j2.nombre} gana la batalla!")
    else:
        print(f"\n¡{pokemon_j2.nombre} se ha debilitado! ¡{pokemon_j1.nombre} gana la batalla!")


def main():
    """Función principal del simulador."""
    print("\n" + "=" * 50)
    print("     SIMULADOR DE BATALLAS POKÉMON (POO)")
    print("=" * 50)
    
    # Selección del modo de juego
    print("\nSeleccione el Modo de Juego:")
    print("1. Jugador vs Jugador (PvP)")
    print("2. Jugador vs Computadora (PvE)")
    
    modo = obtener_entero_valido("> Opción: ", 1, 2)
    
    if modo == 1:
        # Modo PvP
        print("\n" + "=" * 50)
        pokemon_j1 = seleccionar_pokemon("Jugador 1")
        pokemon_j2 = seleccionar_pokemon("Jugador 2")
        batalla_pvp(pokemon_j1, pokemon_j2)
    
    else:
        # Modo PvE
        print("\n" + "=" * 50)
        pokemon_jugador = seleccionar_pokemon("Jugador")
        print("Computadora eligiendo combatiente...")
        pokemon_pc = seleccion_pc()
        batalla_pve(pokemon_jugador, pokemon_pc)
    
    print("\n" + "=" * 50)
    print("          ¡BATALLA FINALIZADA!")
    print("=" * 50)


if __name__ == "__main__":
    main()
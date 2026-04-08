#==========================================
#                 Ejercicio 10
#       Panel de misiones y calculo de 
#                 recompensa
#==========================================

print("=========== VIDEOJUEGO ==========")
print("1. bosque")
print("2. castillo")
print("3. dragón")
print("4. salir")

nombre_jugador = input("Nombre del jugador: ")
clase_jugador = input("Clase del jugador (guerrero, mago, arguero): ")
opcion_mision = input("Opcion de misión: ")
nivel_jugador = int(input("Nivel del jugador: "))
cantidad_derrotados = int(input("Cantidad de enemigos derrotados: "))

match opcion_mision:
    case ("bosque" | "1"):
        if  nivel_jugador >= 1:
            recompensa = cantidad_derrotados * 10
            print("=== Mision bosque completado ===")
            print("Jugador: ", nombre_jugador)
            print("Clase: ", clase_jugador)
            print("Recompensa: ", recompensa)
    case ("castillo" | "2"):
        if nivel_jugador >= 5:
            recompensa = cantidad_derrotados * 20
            print("=== Mision castillo completado ===")
            print("Recompensa base: ", recompensa)
            if clase_jugador == "guerrero":
                bono = 50
                print("Bono adicional: ", bono)
                total = recompensa + bono
                print("Recompensa total: ", total)
            if clase_jugador == "mago":
                bono = 50
                print("Bono adicional: ", bono)
                total = recompensa + bono
                print("Recompensa total: ", total)
            else:
                print("No cumple con el nivel requerido")

    case ("dragón" | "3"):
        if nivel_jugador >= 10:
            recompensa = cantidad_derrotados * 50
            print("=== Mision dragon completado ===")
            print("Recompensa base: ", recompensa)
            if clase_jugador == "guerrero":
                if cantidad_derrotados >= 3:
                    bono = 100
                    print("Bono adicional: ", bono)
            total = recompensa + bono
            print("Recompensa total: ", total)
            if clase_jugador == "arquero":
                if cantidad_derrotados >= 3:
                    bono = 100
                    print("Bono adicional: ", bono)
            total = recompensa + bono
            print("Recompensa total: ", total)
        else:
            print("No cumple con el nivel requerido")
    case _:
        print("No cumple con ninguno de los requisitos")
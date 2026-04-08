# Ejercicio 4
# Ejercicio Integrador
# Una sala de videojuegos vende fichas para poder jugar en las máquinas.
# Cada ficha cuestra 500 colones.
#
# El sistema debe permitir que varios clientes compren fichas durante el día.
# El programa debe:
#
# * 1. Mostrar un menú con las siguientes opciones:
#       *1 - comprar fichas
#       *2 - Salir
#
# * 2. Si el cliente desea comprar fichas:
#       * pedir el nombre del cliente
#       * Pedir cuanto dinero tiene
#       * calcular cuentas fichas puede comprar
#       * calcular cuanto dinero le sobra
#
# * 3. Reglas del sistema:
#       * si el cliente no tiene dinero suficiente para al menos una ficha,
#          el sistema debe indicarlo
#       * si tiene dinero, debe mostrar:
#           Cantidad de fichas que puede comprar
#           Dinero devuelto
# * 4. El programa debe repetirse usando un ciclo while hasta que el usuario elija salir.
# * 5. El cálculo de fichas debe realizarse mediante una función con parámetros y retorno.

def comprar_fichas(dinero):
    fichas_comprar = dinero // 500

    return fichas_comprar

def restante (dinero):
    total = comprar_fichas(dinero) * 500
    devuelto = dinero - total

    return devuelto

def menu():
    print("1. Comprar fichas")
    print("2. Salir")

    opcion = input("Seleccione una opción: ")

    while True:
        match opcion:
            case "1":
                nombre = input("Ingrese su nombre: ")
                dinero = float(input("Ingrese cuando dinero tiene disponible: "))
                cantidad_fichas = comprar_fichas(dinero,)
                dinero_devuelto = restante(dinero)

                if dinero >= 500:
                    print(f"Cantidad de fichas que puede comprar es de: {cantidad_fichas}")
                    print(f"Dinero devuelto: {dinero_devuelto}")
                else:
                    print("No cuenta con dinero suficiente para comprar una ficha")
            case "2":
                print("Saliendo...")
                break
            case _:
                print("Opcion no valida")

        opcion = input("Seleccione un opcion: ")


menu()
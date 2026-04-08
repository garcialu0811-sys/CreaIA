def saludo(nombre):
    print("hola buenos dias!")
    print(f"¿Cómo estas, {nombre}?")

def despedida(nombre):
    print("adios, que tengas un buen dia!")
    print(f"¡Hasta luego, {nombre}!")

def menu():
    print("1. Saludar")
    print("2. Despedirse")
    print("3. Salir")

    opcion = input("Seleccione un opcion: ")

    nombre = input("Ingrese su nombre: ")


    while True:
        match opcion:
            case "1":
                saludo(nombre)
            case "2":
                despedida(nombre)
            case "3":
                print("Saliendo...")
                break
            case _:
                print("Opcion no valida")

        opcion = input("Seleccione un opcion: ")


menu()
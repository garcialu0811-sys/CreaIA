def saludo():
    print("hola buenos dias!")

def despedida():
    print("adios, que tengas un buen dia!")

def realizar_operacion(a, b):
    return a + b

def menu():
    print("1. Saludar")
    print("2. Despedirse")
    print("3. Salir")

    opcion = input("Seleccione un opcion: ")


    while True:
        match opcion:
            case "1":
                saludo()
            case "2":
                despedida()
            case "3":
                print("Saliendo...")
                break
            case _:
                print("Opcion no valida")

        opcion = input("Seleccione un opcion: ")


menu()
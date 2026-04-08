def saludo(nombre):
    print("hola buenos dias!")
    print(f"¿Cómo estas, {nombre}?")

def despedida(nombre):
    print("adios, que tengas un buen dia!")
    print(f"¡Hasta luego, {nombre}!")

def calculo_impuesto(precio):
    impuestos = precio * 0.15
    total = precio + impuestos

    return total

def menu():
    print("1. Saludar")
    print("2. Despedirse")
    print("3. Calcular impuestos")
    print("4. Salir")

    opcion = input("Seleccione un opcion: ")

    nombre = input("Ingrese su nombre: ")


    while True:
        match opcion:
            case "1":
                saludo(nombre)
            case "2":
                despedida(nombre)
            case "3":
                precio = float(input("Ingrese el precio: "))
                precio_total = calculo_impuesto(precio)

                print(f"El precio total con impuestos es: {precio_total}")
            case "4":
                print("Saliendo...")
                break
            case _:
                print("Opcion no valida")

        opcion = input("Seleccione un opcion: ")


menu()
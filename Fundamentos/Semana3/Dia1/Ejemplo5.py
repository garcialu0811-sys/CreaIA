def saludo(nombre):
    print("hola buenos dias!")
    print(f"¿Cómo estas, {nombre}?")

def despedida(nombre):
    print("adios, que tengas un buen dia!")
    print(f"¡Hasta luego, {nombre}!")

def calculo_impuesto(precio, impuesto ):
    impuestos = precio * (impuesto / 100)
    total = precio + impuestos

    return total, impuestos

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
                impuesto =  float(input("Ingrese el impuesto (en porcentaje): "))
                precio_total, porcentaje_impuesto = calculo_impuesto(precio, impuesto)

                print(f"El precio total con impuestos es: {precio_total}")
            case "4":
                print("Saliendo...")
                break
            case _:
                print("Opcion no valida")

        opcion = input("Seleccione un opcion: ")


menu()
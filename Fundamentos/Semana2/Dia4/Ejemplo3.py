opcion = ""

while opcion != "salir" and opcion != "2":
    print("1 - Saludar")
    print("2 - Salir")
    opcion = input("Ingrese una opcion: ")

    if opcion == "1" or opcion == "saludar":
        print("Hola, ¿cómo estas?")
    elif opcion == "2" or opcion == "salir":
        print("Adiós, que tengas un buen día.")
    else:
        print("Opción no válida, por favor ingrese una opcion válida. ")
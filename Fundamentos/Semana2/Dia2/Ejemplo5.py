opcion = input("Seleccione una opcion del 1 al 3 o escriba salir: ")

match opcion:
    case "1":
        print("Registrando producto...")
    case "2":
        print("MOstrando inventario...")
    case "3" | "salir":
        print("Saliendo ...")
    case _:
        print("Opcion invalida")
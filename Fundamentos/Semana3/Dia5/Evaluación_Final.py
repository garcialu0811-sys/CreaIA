inventario = [
    ["Croquetas", 15, 20, 0],
    ["Juguete", 10, 5, 0],
    ["Champu", 5, 12, 0]
]


def vender_un_producto(cantidad):
    for fila in range (len(inventario)):
        for producto in range (len(inventario[fila])):
            # nombre = input("Escriba el nombre del producto: ")
            # cantidad = int(input("¿Cantidad a vender?: "))
            productos_vendida = inventario[fila][producto]

            while True:
                if producto <= cantidad:
                    inventario [fila][producto] -= cantidad
                    print(f"¡Venta exitosa! Quedan {productos_vendida} {inventario[fila][producto]} en el estante")
                else:
                    cantidad = int(input(f"[Error: solo tenemos {inventario[fila][producto]} en stock. Intente de nuevo]: "))
        

def agregar_un_producto(inventario):
    for fila in range(len(inventario)):
        for producto in range (len(inventario[fila])):
            nombre = input("Ingrese el nombre del nuevo producto: ")
            inventario.append[fila][0] = nombre

            cantidad = int(input("Ingrese la cantidad inicial: "))
            inventario.append[fila][1] = cantidad

            precio = float(input("Ingrese el precio unitario: "))
            inventario.append[fila][2] = precio

            print(f"¡Éxito! El producto '{nombre}' ha sido incorporado al inventario.")

def mostrar_estante():
    for fila in range(len(inventario)):
        nombre = inventario[fila][0]
        cantidad = inventario[fila][1]
        precio = inventario[fila][2]

        print(f"- {nombre:10} | Stock: {cantidad:<5} | Precio: ${precio:5}")

def menu():
    print("\n>>>>> SISTEMA DE GESTIÓN HUELLITAS FELICES <<<<<")
    print("\nProductos disponibles")
    
    mostrar_estante()

    opcion = input("\n¿Qué desea hacer? (Vender / Agregar / Eliminar / Salir): ").upper()

    while True:
        match opcion:
            case "Vender":
                nombre = input("Escriba el nombre del producto: ")
                cantidad = int(input("¿Cantidad a vender?: "))

                cantidad_producto = vender_un_producto(nombre, cantidad)

            case "Agregar":
                print("")
                agregar_un_producto()

            case "Eliminar":
                print("")

            case "Salir":
                print("Saliendo...")
                break
            
        opcion = input("¿Qué desea hacer? (Vender / Agregar / Eliminar / Salir): ")

menu()
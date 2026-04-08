# Crear una lista llamada productos donde cada elemnto sea un dicionario.
# los productos van a tener, nombre, precio, cantidad
# despues de ingresar fin, vamos a mostrar el inventario con:
#       nombre - precio - canitdad



def mostrar_inventario(productos):
    # Forma 1:
    print("\nforma1")
    for num_articulo in range(len(productos)):
        print(productos[num_articulo]["nombre"])
        print(productos[num_articulo]["precio"])
        print(productos[num_articulo]["cantidad"])

    # Forma 2:
    print("\nforma2")
    for num_articulo in range(len(productos)):
        # float -> str : 100.5 -> "100.5"
        articulo = productos[num_articulo]["nombre"] + " - " + str(productos[num_articulo]["precio"]) + " - " + str(productos[num_articulo]["cantidad"])
        print(articulo)

    # Forma 3:
    print("\nforma3")
    for num_articulo in range(len(productos)):
        print(f"{productos[num_articulo]["nombre"]} - {productos[num_articulo]["precio"]} - {productos[num_articulo]["cantidad"]}")
    
    # Forma 4:
    print("\nforma4")
    for num_articulo in range(len(productos)):
        print(productos[num_articulo]["nombre"], end=" - ")
        print(productos[num_articulo]["precio"], end=" - ")
        print(productos[num_articulo]["cantidad"])

    #


#Crear la lista
productos = []

while True:
    nombre = input("Ingrese el nombre del producto o ingrese FIN para termianr: ")
    if nombre == "FIN":   #ToDo: mejorar validación
        mostrar_inventario(productos)
        break

    precio = float(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad del producto: "))

    productito = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }

    productos.append(productito)


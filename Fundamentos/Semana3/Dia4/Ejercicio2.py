def mostrar_inventario(lista_productos):
    print("\n========= INVENTARIO FINAL =========")
    
    # Forma 1: Impresión línea por línea (Básico)
    print("\n--- Forma 1: Línea por línea ---")
    for i in range(len(lista_productos)):
        print(lista_productos[i]["nombre"])
        print(lista_productos[i]["precio"])
        print(lista_productos[i]["cantidad"])

    # Forma 2: Concatenación clásica convirtiendo a texto (str)
    print("\n--- Forma 2: Concatenación manual ---")
    for i in range(len(lista_productos)):
        # Necesitamos convertir los números (float, int) a texto (str) para unirlos con el signo +
        articulo = lista_productos[i]["nombre"] + " - $" + str(lista_productos[i]["precio"]) + " - " + str(lista_productos[i]["cantidad"]) + " unds."
        print(articulo)

    # Forma 3: Interpolación f-strings (¡La forma más recomendada y moderna!)
    # Permite inyectar las variables directamente dentro del texto sin convertir tipos manuales.
    print("\n--- Forma 3: Usando f-strings ---")
    for producto in lista_productos: # Usamos un for simplificado
        print(f"{producto['nombre']} - ${producto['precio']} - {producto['cantidad']} unds.")

    # Forma 4: Modificando el final del print (end="")
    print("\n--- Forma 4: Usando parámetro 'end' ---")
    for i in range(len(lista_productos)):
        print(lista_productos[i]["nombre"], end=" - $")
        print(lista_productos[i]["precio"], end=" - ")
        print(lista_productos[i]["cantidad"], "unds.")


# --- PROGRAMA PRINCIPAL ---

productos = [] # Iniciamos con una lista vacía que guardará nuestros diccionarios

print("Bienvenido al sistema de registro de productos.")

while True:
    # Usamos .upper() para que funcione si el usuario escribe "fin", "Fin" o "FIN"
    nombre = input("\nIngrese el nombre del producto (o 'FIN' para terminar): ").upper()
    
    if nombre == "FIN":
        mostrar_inventario(productos)
        break # Rompemos el ciclo infinito

    # Solicitamos los datos numéricos y los convertimos al tipo correcto
    precio = float(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad en bodega: "))

    # Empacamos toda la información de esta vuelta del ciclo en un diccionario
    nuevo_producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }

    # Agregamos la "caja" (diccionario) completa a nuestro "estante" (lista principal)
    productos.append(nuevo_producto)
    print(f"¡Producto '{nombre}' agregado exitosamente!")
# Caja reigstradora
print("Bienvenidos a la tienda")
nombre_producto = input("Ingrese el nombre del producto: ")  #string
precio_producto = float(input("Ingrese el precio del producto: "))  # float, se convierte directamente al peir el input
cantidad_producto = int(cantidad_producto)

#procesamiento de la informaacion
subtotal = precio_producto * cantidad_producto
impuesto = subtotal * 0.15  #suponiendo un impuesto del 15%
total = subtotal + impuesto

#Impresion de los resultados
print("\n--- Resumen de la compra ---")

#%s: string
#%f: float
#%d: int

#print("Nombre del producto: ", nombre_producto)
print("%25s: %10s" %("Nombre del producto", nombre_producto))

#print("Precio del producto: ", precio_producto)
print("%25s: %10.2f" %("Precio del producto", precio_producto))

#print("Cantidad del producto: ", cantidad_producto)
print("%25s: %10d" %("Cantidad del producto", cantidad_producto))


#print("Subtotal: ", subtotal)
print("%25s: %10.2f" %("Subtotal", subtotal))

#print("Impuesto: ", impuesto)
print("%25s: %10.2f" %("Impuesto", impuesto))

#print("Total: ", total)
print("%25s: %10.2f" %("Total", total))


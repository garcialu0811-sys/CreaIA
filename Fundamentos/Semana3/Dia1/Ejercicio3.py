# Ejercicio 3
# Funcion con retorno
# Un supermercado desea calcular el precio final de una compra.
# Cree una funcion llamada `calcular_total(precio, cantidad)` que:
# * Reciba el precio de un producto.
# * Reciba la cantidad comprada.
# * Calcule el total a pagar.
# * Devuelva el resultado al programa principal.

def calcular_total(precio, cantidad):
    total = precio * cantidad

    return total

precio = float(input("Ingrese el precio del producto: "))
cantidad = int(input("Ingrese la cantidad de productos comprados: "))
precio_total = calcular_total(precio, cantidad)

print(f"El total es: {precio_total} ")
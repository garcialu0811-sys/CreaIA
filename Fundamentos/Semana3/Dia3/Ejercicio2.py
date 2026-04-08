#                       Ejercicio 2:
# Eres el encargado de una tienda de abarrotes. Debido a la inflación,
# todos los productos que cuesten menos de 50 pesos deben subir un 10%
# Los productos que ya cuestan 50 o más se quedan igual. Porteriormente, 
# mostrar los precios finales.

# precios_pasillos = [
#     [10.0, 55.0, 20.0],
#     [45.0, 80.0, 12.0],
#     [100.0, 30.0, 48.0]
# ]

def mostrar_precios(precios_pasillos):
    # Ciclo externo, viaja por las filas completas (pisos)
    for fila in precios_pasillos:     
        # Ciclo interno, viaja por cada poroducto dentro de la fila actual
        for producto in fila:
            print("Inventario: ", producto)

precios_pasillos = [
    [10.0, 55.0, 20.0],
    [45.0, 80.0, 12.0],
    [100.0, 30.0, 48.0]
]

# Declarar en una variable el 10% de incremento
porcentaje_incremento = 0.10

# Recorrer la matriz
for fila in range(len(precios_pasillos)):
    for columna in range(len(precios_pasillos[fila])):
        # Aplicar la condición (if) 
        # si el precio es menor a 50 
        if precios_pasillos[fila][columna] <= 50:
            #guardar o modificar el valor en la lista(matriz)
            precios_pasillos [fila] [columna] += precios_pasillos[fila] [columna] * porcentaje_incremento

# Mostrar la matriz ya modificada
mostrar_precios(precios_pasillos)
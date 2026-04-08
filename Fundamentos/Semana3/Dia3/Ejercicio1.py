#        Ejercicio de Repaso
# El inventario de la Tienda de Frutas
# Tiene una lista donde cada sublista representa un estante.
# cada estante tiene cantidades de frutas.
# Debe calcular cuántas frutas totales hay,
# pero solo de aquellas que tengan más de 5 unidades
# y sean un número par

# Lista de estantes con cantidades de productos
# inventario = [
#     [10, 4, 8],
#     [5, 12, 3],
#     [7, 20, 6]
# ]



print("Inventario de la tienda de frutas")

inventario = [
    [10, 4, 8],
    [5, 12, 3],
    [7, 20, 6]
]

total = 0

# Ciclo externo, viaja por las filas completas (pisos)
for fila in inventario:     
    # Ciclo interno, viaja por cada poroducto dentro de la fila actual
    for frutas in fila:
        if frutas > 5 and frutas % 2:
            frutas += frutas
            print(frutas)
            break
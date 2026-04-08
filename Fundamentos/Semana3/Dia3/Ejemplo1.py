def mostrar_productos(estante):
    # Ciclo externo, viaja por las filas completas (pisos)
    for fila in estante:     
        # Ciclo interno, viaja por cada poroducto dentro de la fila actual
        for producto in fila:
            print("Inventario: ", producto)


print("Iniciando inventario ")

estante = [
    ["pizza", "pollo frito", "arroz chino"],
    ["agua", "red bull", "cocacola"]
]

mostrar_productos(estante)

# Recorrer nuestro estante, encontrar el agua y remplazarlo por "vacio", y detener el ciclo

# Ciclo externo, viaja por las filas completas (pisos)
for fila in estante:     
    # Ciclo interno, viaja por cada poroducto dentro de la fila actual
    for producto in fila:
        if producto == "agua":
            fila[fila.index(producto)] = "vacio"
            break

print("="*15)
mostrar_productos(estante)

# manera 2 de hacerlo, usando indices
for fila in range(len(estante)): # 0, 1
    for columna in range(len(estante[fila])):    # 0, 1, 2
        if estante[fila][columna] == "vacio":
            estante[fila][columna] = "pepsi"
            break

print("="*15)
mostrar_productos(estante)
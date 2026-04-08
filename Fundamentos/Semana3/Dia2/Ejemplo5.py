print("Iniciando inventario ")

estante = [
    ["Pizza", "Pollo frito", "Arroz chino"],
    ["Agua", "Red bull", "Cocacola"]
]

# Ciclo externo, viaja por las filas completas (pisos)
for fila in estante:     
    # Ciclo interno, viaja por cada poroducto dentro de la fila actual
    for producto in fila:
        print("Inventario: ", producto)
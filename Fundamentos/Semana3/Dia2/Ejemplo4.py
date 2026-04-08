print(" --- SISTEMA DE BUSQUEDA POR COORDENADAS ---")

bodega = [
    ["Arroz", "Frijoles", "Lentejas"],  #Fila 0: Granos
    ["Atún", "Sardinas", "Sopa"],       #Fila 1: Enlatados
    ["Agua", "Jugo", "Refresco"],       #Fila 3: Bebdias
]

# queremos sacar la sardina
# Paso1. ¿En que fila esta? en la fila 1 (Enlatados)
# Paso2. ¿En que columna esta dentro de esa fila?, en la columna 1
producto_buscado = bodega [1][1]
print("Producto extraído: ", producto_buscado)

# Queremos sacar el "agua". (Fila 2, columna 0)
print("Bebida seleccionada: ", bodega[2][0])

#Modificar un dato: el jugo se agoto, pondremos té
bodega[2][1] = "Té"
print("Fila de bebidas actualizada: ", bodega[2])


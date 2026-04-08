# Listas de listas y diccionarios

## Listas de listas (Matriz)
tambien se conoce como:
- lista de listas
- matrices
- estructura bidimensional
- tabla de filas y comlumnas

Ejemplo conceptal

| producto | precio | cantidad|

representacion en python:
inventario = [["Arroz, 1200, ]]

###2. ¿Como acceder a los datos? (doble indice)

Ambos indices empiezan a contar desde cero `estante_principal[fila][columna]`.



# Recorrer una matriz

Necesitasmo un bucle anidado (un for dentro de otro for). En primer bucle se encarga de bajar por los pisos(filas), y el segundo bucle se encarga de caminar de izquierda a derecha revisando los productos de ese piso(columnas)

```py
for fila in matriz_principal
    for elemento in fila:
```

inventario [fila][columna]

- primer indice -- fila
- segundo indice - columna


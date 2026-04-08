# Uso del break

```python

while True:
    nombre = input("Ingrese su nombre... (salir para terminar): ")

    if nombre == "salir"
    break

```


# Continue
```python
for producto in range(6):
    if producto == 3:
        continue    #Para continuar etiquetando y break para que pare el programa y no siga etiquetando
    print("Producto etiquetado: ", producto)
```

# Estructura de datos
## Lista

## Crear una lista
### Forma 1: con elementos
mi_lista = [10, "hola", 3.14, ]

### Forma 2: Sin elemenos
lista_vacia = []

## Acceder a los elementos

saludi = mi_lista[1]
print(saludo)

### Un paso
print(mi_lista[1])

## Forma 2: Indices negativos
print(mi:list[-1])

## Forma 3: Por porcion de la lista (slicing)
`nombe de la lista` + `[` + `inicio` + `:` + `final` + `]`
mi_lista[1:2]

## Forma 4: slicing con saltos
`nombe de la lista` + `[` + `inicio` + `:` + `final` + `:` + `paso/incremento` + `]`
mi_lista[0:4:2]


# Agregar elementos (`append`)

### sintaxis

`nombre de la lista` + `.` + `append(` + `lo que quiero agregar` + `)`
lista_vacia.append("Diego)

print(lista_vacia[0])


mi_lista.append("Mundo")

print(mi_lista[3])

print(mi_lista)


## Recorer una lista

# Modificar un elemento
mi_lista[1] = "Hola"

# Eliminar un elemento
## Eliminar un elemento por el indice con `del`
del mi_lista[1]

## Eliminar por valor con `remove()`
`nombre de la lista` + `.` + `remove(` + `valor que quiero eliminar` + `)`
mi_lista.remove(10)

## eliminar el ultimo elemento con `pop`
mi_lista.pop


# Estructura de tuplas
la gran diiferencia es que la tupla es inmutable
**sINTAXIS** eN LUGAR DE CORCHETES `[]` (listas), usamos parentesis `()` (tuplas)

# Crear tupla

producto = ("Arroz", 1200, 5)

# Acceder valores

print(productos[0])
print(productos[1])

# Recorrer tuplas

for Producto in productos:
    print(producto)

len(productos)


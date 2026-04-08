## Crear una lista

### Forma 1: con elementos
mi_lista = [10, "hola", 3.14, ]

### Forma 2: Sin elemenos
lista_vacia = []

## Acceder a los elementos
saludo = mi_lista[1]
print(saludo)

### Un paso
print(mi_lista[1])

# Agregar elementos (`append`)
### sintaxis
#`nombre de la lista` + `.` + `append(` + `lo que quiero agregar` + `)`
lista_vacia.append("Diego")

print(lista_vacia[0])

mi_lista.append("mundo")

print(mi_lista)

# Recorrer una lista
#Forma 1: con un ciclo `for`
for elemento in mi_lista:
    print(elemento)

    if elemento == 3.14:
        print("Enconre el numero pi")
        break

#Forma 2: usando los indices
#len(mi_lista) # Devuelve la cantidad de elementos que tiene la lista
for indice in range(len(mi_lista)):
    print(mi_lista[indice])


print(mi_lista[-1])

## Forma 3: Por porcion de la lista (slicing)
#`nombe de la lista` + `[` + `inicio` + `:` + `final` + `]`
print(mi_lista[1:3])


## Forma 4: slicing con saltos
#`nombe de la lista` + `[` + `inicio` + `:` + `final` + `:` + `paso/incremento` + `]`
print(mi_lista[0:4:2])


# Modificar un elemento
mi_lista[1] = "Hola"

print(mi_lista)


## Eliminar por valor con `remove()`
#`nombre de la lista` + `.` + `remove(` + `valor que quiero eliminar` + `)`
mi_lista.remove(10)


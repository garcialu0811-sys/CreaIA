# Estructura de datos
## Diccionarios
se usa lo que se llama "clave y valor" a la caja, y adentro guardamos la infomacion (valor)

```py
clave : valor
```

**Sintaxis:** a diferencia de las listas que usan corchetes`[]`, los diccionarios se crean usando llaves `{ }`. separamos la clave y el valor con dos puntos `:`.

```py
producto = {
    "nombre": "Arroz",
    "precio": 1200.0,
    "cantidad": 5
}
```

un diccionario es ideal cuando queremos que cada dato tenga una etiqueta clara.

# acceder a valores
Para acceder a un valor dentro de un diccionario usamos:

`diccionario["clave"]`

la clave deve existir exactamente igual(respeta mayuscula/minuscula)

```py
producto = {
    "nombre": "Arroz",
    "precio": 1200.0,
    "cantidad": 5
}

print(producto["nombre"])
print(producto["precio"])
print(producto["cantidad"])

total = producto["cantidad"] * producto ["precio"]

print(f"El total de los productos son: {total}")

print(producto)
```

## Modificar los valores en un diccionario
<!-- en una lista -->
lista_edades[5] = 50

<!-- en un diccionario -->
producto["precio"] = 1500

<!-- Actualizar el precio despues de una venta -->
producto["cantidad"] = producto["cantidad"] - 1 


# Agregar un elemento al diccionario
```py
producto["categoria"] = "Granos"
```

# Recorrer un diccionario
### forma 1: solo las claves
```py
for clave in producto:
    print(f"clave: {clave}: valor: {producto[clave]}")

```

### forma 2: utilizando .items()
```py
for clave, valor in producto.items():
    print(f"clave: {clave}: valor: {valor}")
```


*El diccionario es mas claro y legible*

# errores comuner
1. escribir mal la clave
2. Acceder a clave inexistentes
3. confundir lista con diccionario.
4. olvidar que las claves distingen mayusculas






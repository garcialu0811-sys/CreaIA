# Condicinales
## La regla basica: el `if`

bloque condicional del if
    me indica que esto le pertenece al bloque
    esto tambien le pertenece

bloque condicional del if
    me indica que esto le pertenece al bloque
    esto tambien le pertenece


### Sintaxis:
```python

if condicion:
    accion

```

### Ejemplo
```python

dinero = 1000
precio = 750

if dinero >= precio:
    print("Venta aprobada")

```


### Practica guiada
* Programar un sistema de acceso a la bodega de la tienda
```python
print("=== SISTEMA DE SEGURIDAD DE LA BODEGA ===")

clave_ingresada = input("Ingrese la clave de seguridad: ")
clave_correcta = "1234"

if clave_ingresada == clave_correcta:
    print("Clave correcta. Acceso permitido.")
    print("Bienvenido a la bodega super segura")

print("Fin del programa.")
```


## COndicional `else`
* NO LLEVA NUNCA UNA CONDICION AL LADO!
* Es el basurero que recoge cualquier cosa que no haya cumplido con la regla del `if`

## Condicional `elif`

### CONDICIONAL: SWITCH (MATCH/CASE)


### sintaxis 

match valor:
    case patron1:
        # acciones
    case patron2:
        acciones
    case _:
        acciones por defecto



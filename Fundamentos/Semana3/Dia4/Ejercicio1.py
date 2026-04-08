# Crear un diccionario llamado "cliente" con:
# - nombre
# - edad
# - ciudad
# Imprimir cada valor utilizando la sintaxis correcta

# Modificar el diccionario "cliente":
# - Cambiar la ciudad.
# - Aumentar la edad en 1

# Imprimir cada calor utilizando la sintaxis correcta

cliente = {
    "nombre": "Juan",
    "edad": 19,
    "ciudad": "Guatemala"
}

print(cliente["nombre"])
print(cliente["edad"])
print(cliente["ciudad"])

print(cliente)

cliente["ciudad"] = "Mexico"
print(cliente)

cliente["edad"] = cliente["edad"] + 1
print(cliente)
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

# Modiciar un dato en la clave que se desea modificar
producto["precio"] = 1500.0
print(producto)

#Modificar un dato en la clave que se elija aumentando o restando
producto["cantidad"] = producto["cantidad"] - 1 
print(producto)

# Agregar una clave al diccionario
producto["categoria"] = "Granos"
print(producto)

# Recorrer un diccionario forma 1
for clave in producto:
    print(f"clave: {clave}: valor: {producto[clave]}")


total = producto["cantidad"] * producto["precio"]
print(f"El total de los productos son: {total}")

print("="*15)
# Recorrer un diccionario forma 2: ppor items
for clave, valor in producto.items():
    print(f"clave: {clave}: valor: {valor}")

for clave in producto.items():
    print(f"clave: {clave}: ")





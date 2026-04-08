#----- IGNORE ----
# Saludo inicial de la tienda digital
print('==============================')
print('Bienvenido a la tienda digital')
print('==============================')
#print('¿Qué desea compar?')

nombre_producto = input('¿Qué desea compar? ')
edad_cliente = input ('Cual es tu edad? ')

# Opcion 1 | Dos print separados
print('1. El producto que escogio es: ', end= '') # El end='' es para evitar el salto de línea
print(nombre_producto)

# Opcion 2 | Un solo print con formato
print(f'2. El producto que escogio es: {nombre_producto}. Y la edad del cliente es: {edad_cliente}')

# Opcion 3 | Un solo print con concatenación
print('3. El producto que escogio es: ' + nombre_producto)

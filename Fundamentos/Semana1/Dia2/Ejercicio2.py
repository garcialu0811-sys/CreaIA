# Ejercicio 2
# Declarar 3 productos (el usuario da a decir cuales productos)
# Preguntar el precio de cada producto
# Preguntar la cantidad disponible del producto
# Generar una factura de inventario, 
# Encabezado, producto: nombre | precio: ### | Cantidad: #

print('==============================')
print('Bienvenido a la tienda digital')
print('==============================')

Producto1 = input('Menciona el primer producto: ')
Precio1 = input('¿Cual es el precio del primer producto? ')
Disponible1 = input('¿Cuantos tiene en existencia?')

Producto2 = input('Menciona el segundo producto: ')
Precio2 = input('¿Cual es el precio del segundo producto? ')
Disponible2 = input('¿Cuantos tiene en existencia?')

Producto3 = input('Menciona el tercer producto: ')
Precio3 = input('¿Cual es el precio del tercer producto? ')
Disponible3 = input('¿Cuantos tiene en existencia?')


print('==================================================')
print('              Factura de la tienda')
print('==================================================')

print('================== Productos =====================')
print(f'Producto {Producto1:10s} | Precio {Precio1:5s} | Cantidad {Disponible1:5s}')
print(f'Producto {Producto2:10s} | Precio {Precio2:5s} | Cantidad {Disponible2:5s}')
print(f'Producto {Producto3:10s} | Precio {Precio3:5s} | Cantidad {Disponible3:5s}')


print('===== Gracias por su compra, lo esperamos. =====')

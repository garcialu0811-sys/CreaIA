# Ejercicio 1
# Al salir de la tienda, queremos que el sistema le haga 2 preguntas al
# usuario: Su producto favorito y que calificación le da a la tienda (1 a 
# 10). Guarda ambas respuestas y al final imprime un mensaje de despedida.

print('==============================')
print('Bienvenido a la tienda digital')
print('==============================')

nombre_producto = input('¿Qué desea compar? ')
ProductoFavorito = input('¿Cual es su producto favorito? ')
Calificacion = input('¿Del 1 al 10 que califiacion nos da? ')

print(f'El producto que escogio es: {nombre_producto}')
print(f'Su producto favorito es: {ProductoFavorito}')
print(f'La calificación que nos da es: {Calificacion}')

print('=== Gracias por su compra, lo esperamos. ===')
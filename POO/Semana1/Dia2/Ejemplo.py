# Molde ( aun vacio) para la clase Producto
class Producto:
    pass


# Fabricar dos objetos fisicos e independientes
articulo_1 = Producto()
articulo_2 = Producto()

# Les vamos a asignar atributos (caracteristicas) a cada uno
# Sintaxis: objeto.atributo = valor
articulo_1.nombre = "Camiseta"
articulo_1.precio = 19.99
articulo_1.cantidad = 10

articulo_2.nombre = "Pantalon"
articulo_2.precio = 39.99
articulo_2.cantidad = 5

# Mostrar los atributos de cada articulo
print(f"Articulo 1: {articulo_1.nombre} Precio: {articulo_1.precio} Cantidad: {articulo_1.cantidad}")
print(f"Articulo 2: {articulo_2.nombre} Precio: {articulo_2.precio} Cantidad: {articulo_2.cantidad}")

# Ejercicio
# - Una clase producto, que el producto va a tener un nombre y un precio
# - Los productos se deben de sumar, restar y comparar entre ellos para asi poder calificarlos
# - Se debe de crear una seria de 4 productos
# - Se debe de mostrar un resumen al final, que muestre el total en inventario y el producto con mayor precio
# - Deben de usar sobrecarga de operadores

class Producto:
    def __init__(self, nombre_producto, precio_producto):
        self.nombre_producto = nombre_producto
        self.precio_producto = precio_producto

    def __add__(self, otro_producto):
        suma_total = self.precio_producto + otro_producto.precio_producto

        nuevo_producto = f"El nuevo producto agregado es {otro_producto.nombre_producto}"

        return Producto(nuevo_producto, suma_total)
    
    def __sub__(self, otro_producto):
        resta_total = self.precio_producto - otro_producto.precio_producto
        
        producto_restado = f"Producto restado {otro_producto.nombre_producto}"

        return Producto(producto_restado, resta_total)
    
    def __gt__(self, otro_producto):
        return self.precio_producto > otro_producto.precio_producto
    
producto1 = Producto("Arroz", 10)
producto2 = Producto("Frijol", 8)
producto3 = Producto("Azucar", 12)
producto4 = Producto("Fideos", 5)

resumen_final = producto1 + producto2 + producto3 + producto4

print("===== RESUMEN FINAL =====")
print(f"Total inventario: Q {resumen_final.precio_producto}")



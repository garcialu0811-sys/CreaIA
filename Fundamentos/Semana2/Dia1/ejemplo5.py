producto = 5
producto_nombre = "manzana"
precio_manzanas = 500
print("---- Reporte ----")

#Tenemos mas de 10 manzanas?
hay_manzanas = producto > 10
print("¿Hay nás de 10 manzanas? ", hay_manzanas)

#Nos quedamos sin stock en la bodega?
sin_stock = producto == 0
print(f"¿Nos quedamos sin srock en la bodega? {sin_stock}")

#Comparacion de nombres de productos
producto_buscado = "Manzana"
es_manzana = producto_nombre == producto_buscado
print(f"¿EL producto buscado esta en bodega? {es_manzana}")


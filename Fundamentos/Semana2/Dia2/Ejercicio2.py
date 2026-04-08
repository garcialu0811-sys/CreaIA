# EL control de Inventario
# Instrucciones: Escriba un programa que pida la cantidad de cajas de leche
# disponibles en la bodega.
#   * Si la cantidad es mayor a 20, imprime "Inventario saludable"
#   * Si la cantidad esta entre 1 y 20, imprime "Alerta: Hacer pedido al proveedor"
#   * Si la cantidad es exactamente 0, imprime "Urgente: Producto agotado"

cantidad = int(input("¿Cuantas cajas de leche hay disponible en bodega? "))

if cantidad > 20:
    print("Inventario saludable")
elif cantidad >=1:
    print("Alerta: Hacer pedido al proveedor")
elif cantidad == 0:
    print("Urgente: Producto agotado")
    
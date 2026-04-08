#==========================================
#               Ejercicio 9
# Sistema de tienda gamer con promociones
#            y validacion de stock
#==========================================


nombre_cliente = input("Ingrese su nombre: ")
nombre_producto = input("Ingrese nombre del producto: ")
precio_unitario = int(input("Precio unitario del producto: "))
cantidad_deseada = int(input("Cantidad deseada: "))
cantidad_stock = int(input("Cantidad en stock: "))
membresia = input("Tiene membresia gamer ( si / no): ")

if cantidad_deseada > cantidad_stock:
    print("No se puede hacer la venta")
elif cantidad_deseada <= cantidad_stock:
    print("Venta aprobada")
    subtotal = precio_unitario * cantidad_deseada
    print("Subtotal: ", subtotal)
    if subtotal > 50000 and membresia == "si":
        descuento = subtotal * 0.20
        print("Descuento: ", descuento)
        total = subtotal - descuento
        print("Total final: ", total)
    if subtotal > 30000 and membresia == "no":
        descuento = subtotal * 0.10
        print("Descuento: ", descuento)
        total = subtotal - descuento
        print("Total final: ", total)
    else:
        if subtotal < 30000:
            descuento = subtotal * 0
            print("Descuento: ", descuento)
            total = subtotal - descuento
            print("Total final: ", total)
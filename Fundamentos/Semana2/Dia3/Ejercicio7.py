#==========================================
#               Ejercicio 7
# Tarifa del hotel con recargo y descuento
#==========================================

nombre_cliente = input("Nombre del cliente: ")
temporada = input("Temporada (alta, media, baja): ")
cantidad_noches = int(input("Cantidad de noches: "))
precio_base = float(input("Precio base por noche: "))
membresia = input("¿Tiene membresía? (si/no) ")

if temporada == "alta":
    if cantidad_noches >= 3 and membresia == "si":
        print("Cliente: ", nombre_cliente)
        recargo = cantidad_noches * precio_base
        subtotal_recargo = recargo * 0.20
        subtotal = recargo + subtotal_recargo
        print("Subtotal con recargo: ", subtotal)
        descuento = subtotal * 0.15
        print("Descuento aplicado: ", descuento)
        total_final = subtotal - descuento
        print("Total final: ", total_final)
    elif cantidad_noches ==2 and membresia == "si":
        print("Cliente: ", nombre_cliente)
        recargo = cantidad_noches * precio_base
        subtotal_recargo = recargo * 0.20
        subtotal = recargo + subtotal_recargo
        print("Subtotal con recargo: ", subtotal)
        descuento = subtotal * 0.05
        print("Descuento aplicado: ", descuento)
        total_final = subtotal - descuento
        print("Total final: ", total_final)
    else:
        print("Cliente: ", nombre_cliente)
        recargo = cantidad_noches * precio_base
        subtotal_recargo = recargo * 0.20
        subtotal = recargo + subtotal_recargo
        print("Subtotal con recargo: ", subtotal)
        print("No se aplica descuento: ")
        print("Total final: ", subtotal)

elif temporada == "media":
    if cantidad_noches >= 3 and membresia == "si":
        print("Cliente: ", nombre_cliente)
        recargo = cantidad_noches * precio_base
        subtotal_recargo = recargo * 0.10
        subtotal = recargo + subtotal_recargo
        print("Subtotal con recargo: ", subtotal)
        descuento = subtotal * 0.15
        print("Descuento aplicado: ", descuento)
        total_final = subtotal - descuento
        print("Total final: ", total_final)
    elif cantidad_noches ==2 and membresia == "si":
        print("Cliente: ", nombre_cliente)
        recargo = cantidad_noches * precio_base
        subtotal_recargo = recargo * 0.10
        subtotal = recargo + subtotal_recargo
        print("Subtotal con recargo: ", subtotal)
        descuento = subtotal * 0.05
        print("Descuento aplicado: ", descuento)
        total_final = subtotal - descuento
        print("Total final: ", total_final)
    else:
        print("Cliente: ", nombre_cliente)
        recargo = cantidad_noches * precio_base
        subtotal_recargo = recargo * 0.10
        subtotal = recargo + subtotal_recargo
        print("Subtotal con recargo: ", subtotal)
        print("No se aplica descuento: ")
        print("Total final: ", subtotal)

else:
    if cantidad_noches >= 3 and membresia == "si":
        print("Cliente: ", nombre_cliente)
        subtotal = (cantidad_noches * precio_base)
        print("Subtotal: ", subtotal)
        descuento = subtotal * 0.15
        print("Descuento aplicado: ", descuento)
        total_final = subtotal - descuento
        print("Total final: ", total_final)
    elif cantidad_noches ==2 and membresia == "si":
        print("Cliente: ", nombre_cliente)
        subtotal = (cantidad_noches * precio_base)
        print("Subtotal: ", subtotal)
        descuento = subtotal * 0.05
        print("Descuento aplicado: ", descuento)
        total_final = subtotal - descuento
        print("Total final: ", total_final)
    else:
        print("Cliente: ", nombre_cliente)
        subtotal = (cantidad_noches * precio_base)
        print("Subtotal: ", subtotal)
        print("No se aplica descuento: ")
        print("Total final: ", subtotal)
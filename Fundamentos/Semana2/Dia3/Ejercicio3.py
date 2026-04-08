#=======================================
#             Ejercicio 3
#       Clasificación de envío
#=======================================

peso = float(input("¿Cual es el peso del paquete? "))

if peso < 1:
    print("Paquete liviano.")
elif peso > 5:
    print("Paquete pesado.")
else:
    print("Paquete estándar.")
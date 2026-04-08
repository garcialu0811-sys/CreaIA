# Ejercicio
# Un cine desea automatizar una parte de su sistema de control de acceso
# el sistema debe de verificar si una persona puede ingresar a una pelicula para mayores de edad (18+)
# 
# El programa debe de solicitar al usuario:
#   * Edad de la persona
#   * Si posee entrada comprada (responder un si o no)
#
# si la persona tiene 18+ y tiene entrada, puede ingresar a la pelicula
# en caso contrario, no se permite la entrada


print("=== SISTEMA DE CONTROL DE ACCESO CINE ===")

edad = int(input("¿Cual es su edad? "))
entrada = input("¿Ya compro su entrada? (si/no): ") == "si"

acceso = (edad >= 18) and entrada

if acceso:
    print("Puede ingresar a ver la pelicula")
else:
    print("No puede ingresar a ver la pelicula")

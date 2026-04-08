#=======================================
#             Ejercicio 2
#    Control de entrada a un torneo
#=======================================

nombre = input ("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
inscripcion = input("Tiene inscripción confirmada (si/no): ")

if edad >= 15 and inscripcion == "si":
    print("Participante autorizado para ingresar al torneo.")
else:
    print("Participante no autorizado")

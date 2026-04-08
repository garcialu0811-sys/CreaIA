#Ejericio 2
#Crear un sistema que:
# Pida edad
# Pida si tiene memebresía premium (si/no)
# Evaluar si puede entrar a la sala exclusiva (Mayor de edad(18+) y membresía)

print("Ejercicio")

#Datos del cliente
edad = 18
membresia = True

mayor_edad = edad >= 18
print("¿Tiene mas de 18 años? ", mayor_edad)

tiene_membresia = membresia
print("¿Tiene una membresia? ", tiene_membresia)

es_mayor = (edad >= 18) and (membresia == True)
print(f"¿Puede ingresar? {es_mayor}")


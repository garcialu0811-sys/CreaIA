#Forma 1: Converir despues de preguntar
cantidad = input("Cuantos cafes deseas comprar? ")
cantidad = int(cantidad)

#Forma 2: Convertir directamente al pedir el input
precio = float(input("Cual es el precio del cafe? "))
precio = float ("10.5")
precio = 10.5

print("Precio de cafe: ", precio, "Tipo:", type(precio))

valor1 = 10
valor2 = 3

#division normal
resultado = valor1 + valor2  # Resultado es un float, aunque ambos valores sean enteros, 5.0

#division entera
resultado_entero = valor1 // valor2  # Resultado es un int, auque ambos valores sean enteros, 5

#Modulo o resto de la division
resto = valor1 % valor2 #Resultado es un int. auque ambos valores sean enteros, 1

print("Resultado de la division: ", resultado)
print("Resultado de la division entera: ", resultado_entero)
print("Resto de la division:"), resto

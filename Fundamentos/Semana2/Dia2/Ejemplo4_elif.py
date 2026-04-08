edad = int(input("Digite su edad: "))
precio_entrada = 2000

if edad <= 12:
    print("El cliente es un niño, tiene un descuento del 50%")
    total = precio_entrada * 0.5
elif edad >= 60:
    print("El cliente es un adulto mayo , tiene un descuento del 25%")
    total = precio_entrada * 0.75
else:
    print("El cliente es un adulto, no tiene descuento")
    total = precio_entrada

print("El precio total de la entrada es: ", total)
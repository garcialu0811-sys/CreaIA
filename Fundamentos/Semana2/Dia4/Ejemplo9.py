total = 0.0

for articulo in range (4):
    precio = float(input("Ingrese el precio del articulo: "))
    #total = total + precio
    total += precio

print("EL total a pagar es: ", total)
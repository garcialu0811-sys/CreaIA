class Camion:
    pass

class CentroLogistico:
    pass

camion1 = Camion()
camion2 = Camion()
camion3 = Camion()
camion4 = Camion()
camion5 = Camion()

garaje_principal = [camion1, camion2, camion3, camion4, camion5]
impuesto = 500

for camiones in range(len(garaje_principal)):
    impuesto_total = camiones * impuesto
    print("El impuesto es de: ", impuesto_total)

for recorrer in garaje_principal:
    print(id(recorrer))

if camiones > 4:
    print("\n¡Capacidad de excedida! Debes mover camiones a otra sucursal")
else:
    print("\nCapacidad óptima")
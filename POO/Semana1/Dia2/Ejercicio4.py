# EJERCICIO CAJA REGISTRADORA

class CajaRegistradora:
    print("\tCAJA REGISTRADORA")
    def cobrar_producto(self):
        precio = float(input("Ingrese el precio del producto: "))
        self.dinero_acumulado += precio
        print(f"Cobro exitoso. Llevamos acumulado: {self.dinero_acumulado}")

    def imprimir_cierre_turno(self):
        print(f"\nNombre del encargado {self.cajero_asignado}, dinero total recaudado en el dia: {self.dinero_acumulado}")
        

caja_express = CajaRegistradora()
caja_express.cajero_asignado = "Delmy"
caja_express.dinero_acumulado = 0
caja_express.cobrar_producto()
caja_express.cobrar_producto()
caja_express.imprimir_cierre_turno()



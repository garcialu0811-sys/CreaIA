# Ejericio 2:
# Caja registradora
# * Crear una clase caja registradora
# * Dentro de nuestra clase, camos a crear 2 métodos
#       - mostrar_dinero_actual: imprimir el dinero actual
#       - procesar_venta(): todas nuestras ventas son de 500. Añadir a nuestro dinero actual, los 500 de ganacia
# * Fabricar una caja registradora
# * Le asignamos dinero inicial
# * Ponemos a trabajar nuestra caja registradora
#       - muestre el dinero
#       - procese una venta
#       - muestre el dinero

class CajaRegistradora:
    def mostrar_dinero_actual(self):
        print(f"Mi dinero actual es de: {self.dinero_inicial}")

    def procesar_venta(self):
        print(f"La venta es de: {self.venta}")
        print(f"Mi dinero actual es de: {self.total_venta}")


caja_1 = CajaRegistradora()
caja_1.dinero_inicial = 0
caja_1.venta = 500
caja_1.mostrar_dinero_actual()

ventas = CajaRegistradora()
ventas.venta_total = caja_1.dinero + caja_1.venta
ventas.procesar_venta()

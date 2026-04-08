# Ejercicio

class Cajero:
    def __init__(self, nombre_empleado, id_empleado):
        self.nombre = nombre_empleado
        self.id = id_empleado
        self.dinero_de_caja = 0

    def cobrar_articulo(self, precio_del_articulo):
        self.dinero_de_caja += precio_del_articulo

    def mostrar_dinero(self):
        print(f"El dinero que hay en caja es: {self.dinero_de_caja}, empleado: {self.nombre}, id del empleado: {self.id}")


cajero1 = Cajero("Manuel", "A001")
cajero1.cobrar_articulo(55)
cajero1.cobrar_articulo(35)
cajero1.mostrar_dinero()

cajero2 = Cajero("Rebeca", "A002")
cajero2.cobrar_articulo(78)
cajero2.mostrar_dinero()

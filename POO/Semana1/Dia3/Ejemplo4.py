class Cliente:

    # El país por defecto sera Guatemala, a menos que nos diga lo contrario
    def __init__(self, nombre, pais="Guatemala"):
        self.nombre = nombre
        self.pais = pais

    # def mostrar_cliente(self):
    #     print(f"\nNombre: {self.nombre} \nPaís: {self.pais}")


# Usando constructor normal
cliente1 = Cliente("Diego", "Costa Rica")
cliente2 = Cliente("Delmy")
cliente3 = Cliente("Panama")

# cliente1.mostrar_cliente()
# cliente2.mostrar_cliente()
# cliente3.mostrar_cliente()
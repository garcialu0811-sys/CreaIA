class Alcancia:
    # Al nacer, no pide ingredientes (atributos) nuevos
    def __init__(self):
        self.dinero_guardado = 0
    
    #
    def depositar_dinero(self, cantidad):
        # Sumar el parametro al atributo
        self.dinero_guardado += cantidad

    def mostrar_ahorros(self):
        print(f"El dinero ahorrado es: {self.dinero_guardado}")

# Crear un objeto
mi_chanchito = Alcancia()

# Acciones
mi_chanchito.depositar_dinero(500)
mi_chanchito.depositar_dinero(1200)
mi_chanchito.mostrar_ahorros()


alcancia1 = Alcancia()
alcancia1.depositar_dinero(5000)
alcancia1.mostrar_ahorros()
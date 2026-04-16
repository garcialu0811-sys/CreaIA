class Motor:
    def __init__(self, caballos_fuerza):
        self.caballos = caballos_fuerza
        self.endendido = False

    def arrancar(self):
        self.encendido = True
        print("Encendiendo el motor")

# El contenedor (guarda la pieza en su interior)
class Auto:
    def __init__(self, marca, modelo, potencia_motor):
        self.marca = marca
        self.modelo = modelo

        self.corazon_mecanico = Motor(potencia_motor)

    def encender_auto(self):
        print("Girando la llave para encender...")

        self.corazon_mecanico.arrancar()

mi_carro = Auto("Toyota", "Corolla", 200)
mi_carro.encender_auto()

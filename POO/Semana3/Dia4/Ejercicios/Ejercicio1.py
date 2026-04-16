class Bateria:
    def __init__(self):
        self.porcentaje = 100

    def descargar(self):
        self.porcentaje -= 10

        print(f"Batería al {self.porcentaje}%")

class Celular:
    def __init__(self, marca):
        self.marca = marca 
        self.energia = Bateria()

    def usar_app(self):
        print("Abriendo aplicación...")

        self.energia.descargar()

celular1 = Celular("Samsung")
celular1.usar_app()
celular1.usar_app()
class Arma:
    def __init__(self, nombre_arma, puntos_daño):
        self.nombre_arma = nombre_arma
        self.puntos_daño = puntos_daño

class Guerrero:
    def __init__(self, nombre_guerrero, arma_equipada):
        self.nombre_guerrero = nombre_guerrero
        self.arma = arma_equipada
    
    def atacar(self):
        print(f"{self.nombre_guerrero} ataca con {self.arma.nombre_arma} causando {self.arma.puntos_daño} de daño")


arma1 = Arma("Espada Larga", 50)
print(f'{" GUERRERO ":=^50}')
guerrero1 = Guerrero("Marcos", arma1)
guerrero1.atacar()

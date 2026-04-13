# 1. El padre
class Animal:
    def comer(self):
        print("El animal esta comiendo")

# 2. El hijo (hereda del padre usando parentesis)
class Perro(Animal):
    pass

# 3. Uso
mi_mascota = Perro()
mi_mascota.comer()
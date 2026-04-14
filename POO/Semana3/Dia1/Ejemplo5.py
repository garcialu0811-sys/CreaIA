class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def __str__(self):
        return f"Animal: {self.nombre}"
    
    def hacer_sonido(self):
        print(f"{self.nombre} hace un sonido genérico.")

class Perro(Animal):
    def hacer_sonido(self):
        print(f"{self.nombre} | El perro hace: Guau, Guauuuu")
    
class Gato(Animal):
    def hacer_sonido(self):
        print(f"{self.nombre} | El gato hace: Miau, Miauuu")

class Pato(Animal):
    def hacer_sonido(self):
        print(f"{self.nombre} | El pato hace: Cuac, Cuac")

animal1 = Perro("Peludo")
animal2 = Gato("Pelusa")
animal3 = Pato("Pancho")

lista_granja  =[animal1, animal2]
lista_granja.append(animal3)

animal_desconocido = Animal("Extraterrestre")

lista_granja.append(animal_desconocido)

print(animal1)

for animal in lista_granja:
    animal.hacer_sonido()

for animal in lista_granja:
    print(animal)
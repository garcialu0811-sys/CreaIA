from abc import ABC, abstractmethod
class Personaje(ABC):
    
    @abstractmethod
    def atacar(self):
        pass

# Modelos concretos
class Guerrero(Personaje):
    def atacar(self): return "Ataca con espada"

class Mago(Personaje):
    def atacar(self): return "Ataca con magia"

# La fabrica (el corazon del patron)
class FabricaPersonajes:

    @staticmethod
    def crear_personaje(tipo):
        # Este metodo centraliza toda la lógica de creacion
        tipo = tipo.lower() # Pasar el tipo a minuscula

        if tipo == "guerrero":
            return Guerrero()
        elif tipo == "mago":
            return Mago()
        else:
            # Hace que el codigo falle, lance una excepcion
            raise ValueError(f"La fabrica no sabe crear: {tipo}")

try:
    eleccion = input("Qué personaje deseas: (Guerrero / Mago) ")
    # el main NO hace: if eleccion == "guerrero: Guerrero()"
    heroe = FabricaPersonajes.crear_personaje(eleccion)
    print(heroe.atacar())
except ValueError as error:
    print(error)

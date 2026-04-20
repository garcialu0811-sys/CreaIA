# arquitectura de software
## Factory (La fabrica)
```py
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


# namespace
#personaje = FabricaPersonajes.crear_personaje("mago")
```


# Modelo - Vista - Controlador (MVC)
## Las 3 cpas
* Modelo (Modle): Es el cerebro. Solo contiene los datos, reglas matematicas y de validacione.
* Vista (View): Es la cara. Solo sabe mostrar texto y capturar lo que el usuario digita. 
* Controlador (Controller): Es el director de la orquesta. Toma los datos de la vista, los procesa en el Modelo y le devuelve el resultado a la vista para que lo imprima.

![](sed.jpeg) para agregar imagen


```py
# MODELO (Logica pura)
class ModeloTarea:
    def __init__(self, descipcion):
        self.descripcion = descripcion
        self.completada = False

# VISTA
class VistaTarea:
    @staticmethod
    def mostra_menu():
        print("\n 1. Agregar tarea\n2. Mostrar Tares \n Salir")
        return input("Opcion: ")

    @staticmethod
    def mostrar_lista(lista):
        print("\nLista de tareas: ")

        for tarea in lista:
            print(f"{tarea.descripcion} está en estado: {tarea.completada}")

# CONTROLADOR
class ControladorTareas:
    def __init__(self):
        self.tareas = []
        self.vista = VistaTarea()

    def ejecutar(self):
        while true:
            opcion = self.vista.mostrar_menu()
            if opcion == "1":
                
```
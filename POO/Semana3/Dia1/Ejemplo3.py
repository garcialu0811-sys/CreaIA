class Persona:
    def __init__(self, nombre):
        # El padre hace su trabajo, inicializa el nombre
        self.nombre = nombre

class Estudiante(Persona):
    def __init__(self, nombre_ingresado, nota_ingresada):
        super().__init__(nombre_ingresado)
        self.nota = nota_ingresada

    def mostrar_info(self):
        print(f"Hola, mi nombre es: {self.nombre} y mi nota es: {self.nota}")

estudiante1 = Estudiante("Juan", 8.5)
estudiante1.mostrar_info()
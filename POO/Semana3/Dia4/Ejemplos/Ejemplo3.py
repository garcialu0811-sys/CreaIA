class Estudiante:
    def __init__(self, nombre, carnet):
        self.nombre = nombre
        self.carnet = carnet

class Curso:
    def __init__(self, nombre_curso):
        self.nombre_curso = nombre_curso

        self.lista_matriculados = []

    def matricular(self, nuevo_estudiante):
        self.lista_matriculados.append(nuevo_estudiante)

        print(f"Sistema: {nuevo_estudiante.nombre} matriculado con éxito")
    
    def pasar_lista(self):
        for alumno in self.lista_matriculados:
            print(f"- {alumno.carnet}: {alumno.nombre}")

alumno1 = Estudiante("Luis","A001")
alumno2 = Estudiante("Keyla", "A002")

curso_poo = Curso("POO")

curso_poo.matricular(alumno1)
curso_poo.matricular(alumno2)
curso_poo.pasar_lista()

curso_poo.lista_matriculados[0].nombre = "Luis Fernando"
curso_poo.pasar_lista()
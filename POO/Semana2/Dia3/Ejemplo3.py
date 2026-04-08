class RegistroVisitante:
    # Atributo de clase: el total o contador de personas
    total_personas = 0

    def __init__(self, nombre_visitante):
        self.nombre = nombre_visitante
        
        # self.total_personas = 1    Error comun

        RegistroVisitante.total_personas += 1
        # RegistroVisitante.total_personas = RegistroVisitante.total_personas + 1 equivalente a la línea de arriba

        print(f"[{self.nombre} ha ingresado]. La pizarra global ahora marca: {RegistroVisitante.total_personas}") 

# nace el primer objeto, la pizarra sube a 1
persona1 = RegistroVisitante("Juan")

# nace el segundo objeto, la pizarra sube a 2     
persona2 = RegistroVisitante("María")

# nace el tercer objeto, la pizarra sube a 3
persona3 = RegistroVisitante("Pedro")

print(f"\nTotal final del dia de personas es: {RegistroVisitante.total_personas}")
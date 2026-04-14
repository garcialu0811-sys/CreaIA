class PersonaMayor:
    def saludar(self):
        print("Buenas tardes estimado, cómo se encuentra usted eldía de hoy, es un placer saludarlo.")
    
class Adolecente(PersonaMayor):
    def saludar(self):
        print("Hola, todo bien?")

senor = PersonaMayor()
chico = Adolecente()

senor.saludar()
chico.saludar() 

# Ejercicio rápido
# Esta programando el sistema de combate de un juego de stae wars. Necesitas gestionar la energía de los Sables de Luz
# * INSTRUCCIONES
# 1. Importa la libreria ramndom como rd
# 2. Crea la clase SableDeLuz con un atributo energia (mpieza en 100)
# 3. Sobrecarga de metodo (recargar): * Si se llama sin argumentos, recupera 10 de energía
#    Si se llama con un número, recupera esa cantidad específica.
# 4. Sobrecarga de operador (-): al restar un SableDeLuz con otro otro objeto SableDeLuz, se bede reducir su energia -10 a no de ellos
# 5. Funcion log y úsalo para mostrar el estado final

import random as rd

class SableDeluz:
    def __init__(self):
        self.enerigia = 100
        
    def recargar(self, cantidad):
        numero = cantidad
        if cantidad == numero:
            print(f"Recupero {numero} de energia")
        
        else:
            print(f"Se llamo sin argumentos, ha recuperado 10 de energia")

    def __sub__(self, sable_de_luz):
        sable_de_luz = 10
        self.enerigia = sable_de_luz - sable_de_luz

        print(f"Se ha restado {sable_de_luz} a Sable De Luz")


sable1 = SableDeluz()
sable1.__sub__("Sable de Luz")
sable1.recargar(20)

print(f"Energía total del sable")

# EJERCICIO
# **INSTRUCCIONES**
# 1. Creen una clase abstracta `Trabajador` con un método abstracto `realizar_tarea()`
# 2. Creen una clase hija `Ingeniero` que sobrescriba `realizar_tarea()` imprimiendo *Diseñando planos*
# 3. Creen una clase hija `Medico` que herede de Trabajador pero No sobreescriba el método. Intencionalmente dejelo con "pass"
# 4. Intente instanciar a ambos

from abc import ABC, abstractmethod

class Trabajador(ABC):

    @abstractmethod
    def realizar_tarea(self):
        pass

class Ingeniero(Trabajador):
    def realizar_tarea(self):
        print("Diseñando planos")

class Medico(Trabajador):
    def realizar_tarea(self):
        pass


trabajador1 = Ingeniero()
trabajador1.realizar_tarea()

trabajador2 = Medico()
trabajador2.realizar_tarea
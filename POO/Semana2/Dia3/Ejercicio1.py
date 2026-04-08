# Ejercicio
# * Crea una clase "Empleado" con un atributo privado "__salario" que inicie en 300
# * Usa "@property" para poder leerlo. Usa `@salario.setter` para permitir cambiarlo, pero SOLO si el nuevo salario es mayor a 300

class Empleado:
    def __init__(self):
        self.__salario = 300
    
    @property
    def salario(self):
        return self.__salario
    
    @salario.setter
    def salario(self, nuevo_salario):
        if nuevo_salario > 300:
            print("Nuevo salario actualizado")
            self.__salario = nuevo_salario
        else:
            print("Salario invalido")

empleado1 = Empleado()

print(empleado1.salario)
empleado1.salario = 450
print(empleado1.salario)
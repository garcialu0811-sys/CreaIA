# Ejercicio:
# La tienda se esta expandiendo y necesitamos a tres personas.
# * Crea una clase llamada "Empleado" usando la palabra pass
# * Fabrica tres objetos físicos independientes y guardalos en las variables
#   "empleado_1", "empleado_2" y "empleado_3".
# * A cada objeto, pegale tres etiquetas (Atributos) "nombre", "cargo", "salario"
# * Inventa los datos. El primero debe ser un Gerente, el segundo un Cajero y el tercero un Bodeguero
# * Finalmente, utiliza la funcion "print()" con f-strinf para imprimir una oracion de presentacion para
#   cada uno, accediendo a sus atributos internos.


class Empleado:
    pass

empleado_1 = Empleado()
empleado_2 = Empleado()
empleado_3 = Empleado()

empleado_1.nombre = "Juan"
empleado_1.cargo = "Gerente"
empleado_1.salario = 3000

empleado_2.nombre = "Marcos"
empleado_2.cargo = "Cajero"
empleado_2.salario = 2500

empleado_3.nombre = "Anderson"
empleado_3.cargo = "Bodeguero"
empleado_3.salario = 2000

print(f"Empleado 1: {empleado_1.nombre} Cargo: {empleado_1.cargo} Salario: ${empleado_1.salario}")
print(f"Empleado 2: {empleado_2.nombre} Cargo: {empleado_2.cargo} Salario: ${empleado_2.salario}")
print(f"Empleado 3: {empleado_3.nombre} Cargo: {empleado_3.cargo} Salario: ${empleado_3.salario}")

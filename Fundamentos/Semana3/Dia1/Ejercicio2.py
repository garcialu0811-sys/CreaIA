# Ejercicio 2
# Funcion con paramentros
# Un sistema de gimnasio desea saludar a cada cliente por su nombre.
#
# Cree una función llamada `saludar_cliente(nombre)` que reciba el nombre del cliente como parámetro e imprima el siguiente mensaje:
# ```
# Hola Diego, bienvenido al gimnasio
# ```

def  saludar_cliente(nombre):
    print(f"Hola {nombre}, bienvenido al gimnasio")

nombre = input("Ingrese su nombre: ")

saludar_cliente(nombre)
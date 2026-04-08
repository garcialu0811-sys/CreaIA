# Ejercicio practico 2
# Vamos a comprobar que la computadora realmente obedece el nuevo paradigma. 
# Vamos a crear facturas a partir de un mismo molde y le pediremos a Python
# que nos demuestre, con pruebas fisicas de la memoria, que cada factura es
# un documento único e irrepetible

# * Crea una clase llamada "FacturaEMitida" usando "pass".
# * Crea una segunda clase llamada "TerminalDePago" usando "pass".
# * Fabrica dos objetos de la clases "FacturaEmitida" y guardalos 
#   en las variables "factura_001" y "factura_002".
# * Fabrica un objeto de la clase "TerminalDePago" llamado "terminal_principal"
# * Usa la funcion "type()" dentro de un "print()" para que 
#   Python te diga que tipo de molde uso para fabricar "terminal_principal"
# * Usa la funcion id() para imprimir el numero de cedula(direccion de memoria) 
#   de "factura_001" y luego el de "factura_002"
# * Evaluar si el id de "factura_001" es ifual al de id de "factura_002" 
#   e imprimir el resultado.

class FacturaEmitida:
    pass

class TerminalDePago:
    pass

factura_001 = FacturaEmitida()
factura_002 = FacturaEmitida()
print(factura_001)
print(factura_002)

print("\n Direccion de memoria")
print(id(factura_001))
print(id(factura_002))

terminal_principal = TerminalDePago()
print(terminal_principal)

print("\n Tipo de molde")
print(type(terminal_principal))

if (id(factura_001)) == (id(factura_002)):
    print("Es igual")
else:
    print("No es igual")


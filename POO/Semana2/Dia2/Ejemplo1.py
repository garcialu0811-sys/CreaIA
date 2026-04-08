class Cuenta:
    def __init__(self, saldo_inicial):
        self.nombre = "Pública"
        self.__saldo = saldo_inicial

mi_cuenta = Cuenta(1000)
print(mi_cuenta.nombre)
print(mi_cuenta.__saldo) # ERROR, python no permite acceder a atributos privados desde fuera de la clase

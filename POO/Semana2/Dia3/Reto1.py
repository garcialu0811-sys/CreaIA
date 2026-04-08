class CuentaBancaria:
    tasa_interes_global = 0.05
    total_cuentas_creadas = 0

    def __init__(self, nombre_titular):
        self.nombre = nombre_titular
        self.__titular = nombre_titular
        self.__saldo = 0
        CuentaBancaria.total_cuentas_creadas += 1

    @property
    def saldo(self):
        pass
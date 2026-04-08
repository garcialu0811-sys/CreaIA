class CuentaBancaria:
    tasa_interes_global = 0.05
    total_cuentas_creadas = 0

    def __init__(self, nombre_titular):
        self.nombre = nombre_titular
        self.__titular = nombre_titular
        

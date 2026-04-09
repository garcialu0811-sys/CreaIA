class CuentaBancaria:
    tasa_interes_global = 0.05
    total_cuentas_creadas = 0

    def __init__(self, nombre_titular):
        self.nombre = nombre_titular
        self.__titular = nombre_titular
        self.__saldo = 0.0
        CuentaBancaria.total_cuentas_creadas += 1

    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def titular(self):
        return self.__titular
    
    @titular.setter
    def titular(self, nuevo_titular):
        #La validación debe asegurar que el nombre no esté en blanco
        if nuevo_titular.strip() == "":
            print("El nombre del titular no puede estar en blanco.")
        else:
            self.__titular = nuevo_titular
    
    def depositar(self, cantidad):
        #Si la cantidad es mayor a 0, súmala al saldo 
        if cantidad > 0:
            self.__saldo += cantidad
        else:
            print("La cantidad a depositar debe ser mayor a 0.")
            
    def retirar(self, cantidad):
        # Solo permite el retiro si hay suficiente dinero en la cuenta.
        if cantidad > self.__saldo:
            print("Fondos insuficientes para retirar.")
        elif cantidad <= 0:
            print("La cantidad a retirar debe ser mayor a 0.")
        else:
            self.__saldo -= cantidad
            
    def proyectar_interes(self):
        # CEste método debe multiplicar el saldo privado actual por la `tasa_interes_global` de la clase e imprimir cuánto dinero ganará el cliente este *año*.
        interes_ganado = self.__saldo * CuentaBancaria.tasa_interes_global
        print(f"Con la tasa de interés actual del {CuentaBancaria.tasa_interes_global*100}%, el interés ganado este año sería: {interes_ganado:.2f}")
    
    @classmethod
    def modificar_tasa_interes(cls, nueva_tasa):
        # Este método debe actualizar la tasa global del banco.
        if nueva_tasa < 0:
            print("La tasa de interés no puede ser negativa.")
        else:
            cls.tasa_interes_global = nueva_tasa
            

cuenta1 = CuentaBancaria("Alice")
cuenta2 = CuentaBancaria("Bob")

#Imprime cuántas cuentas existen a nivel global.
print(f"Total de cuentas creadas: {CuentaBancaria.total_cuentas_creadas}")

# Deposítale 10,000 a cuenta1
cuenta1.depositar(10000)

#Proyecta el interés de cuenta1 con la tasa actual del 5%
cuenta1.proyectar_interes()

# Usa el método de clase para que el Banco suba la tasa de interés a 0.10 (10%).
CuentaBancaria.modificar_tasa_interes(0.10)

# Vuelve a proyectar el interés de cuenta1 para ver cómo la ganancia se duplicó automáticamente.
cuenta1.proyectar_interes()

# Intenta cambiar el nombre de Sofía a un texto en blanco `""` para comprobar que el setter la bloquea.
cuenta1.titular = "" 
print(f"Titular actual de cuenta1: {cuenta1.titular}")   
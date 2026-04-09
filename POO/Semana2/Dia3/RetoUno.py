# Crea la clase `CuentaBancaria`.
class CuentaBancaria:
    # El banco maneja una `tasa_interes_global` que nace en `0.05`
    tasa_interes_global = 0.05
    # El banco lleva un registro de `total_cuentas_creadas` que nace en `0`.
    total_cuentas_creadas = 0

    # Crear el constructor que reciba el nombre del titular y lo asigne a un atributo privado.
    def __init__(self, nombre_titular):
        self.nombre = nombre_titular
        # Crea el atributo privado `__titular` usando el parámetro.
        self.__titular = nombre_titular
        # Crea el atributo privado `__saldo` e inicialízalo por defecto en `0.0`.
        self.__saldo = 0.0
        # Súmale 1 al atributo de clase `total_cuentas_creadas`
        CuentaBancaria.total_cuentas_creadas += 1
    
    # Crea un `@property` llamado `saldo` que actúe como Getter
    @property
    def saldo(self):
        return self.__saldo
    
    # Crea un `@property` llamado `titular` (Getter).
    @property
    def titular(self):
        return self.__titular
    
    # Crea su respectivo `@titular.setter`.
    @titular.setter
    def titular(self, nuevo_titular):
        # La validación debe asegurar que el nombre no esté en blanco
        if nuevo_titular == "":
            print("El nombre del titular no puede estar en blanco.")
        else:
            self.__titular = nuevo_titular
    
    # Crea un método `depositar(self, cantidad)`.
    def depositar(self, cantidad):
        # Si la cantidad es mayor a 0, súmala al saldo 
        if cantidad > 0:
            self.__saldo += cantidad
        else:
            print("La cantidad a depositar debe ser mayor a 0.")

    # Crea un método `retirar(self, cantidad)`.        
    def retirar(self, cantidad):
        # Solo permite el retiro si hay suficiente dinero en la cuenta.
        if cantidad > self.__saldo:
            print("Fondos insuficientes para retirar.")
        elif cantidad <= 0:
            print("La cantidad a retirar debe ser mayor a 0.")
        else:
            self.__saldo -= cantidad

    # Crea un método `proyectar_interes(self)`.        
    def proyectar_interes(self):
        # Multiplicar el saldo privado actual por la `tasa_interes_global` de la clase
        interes_ganado = self.__saldo * CuentaBancaria.tasa_interes_global
        # Imprimir cuánto dinero ganará el cliente este *año*.
        print(f"Con la tasa de interés actual del {CuentaBancaria.tasa_interes_global*100}%, el dinero a ganar este año sera de: {interes_ganado:.2f}")
    
    # Crea un `@classmethod` llamado `modificar_tasa_interes(cls, nueva_tasa)`.
    @classmethod
    def modificar_tasa_interes(cls, nueva_tasa):
        # Este método debe actualizar la tasa global del banco.
        if nueva_tasa < 0:
            print("La tasa de interés no puede ser negativa.")
        else:
            cls.tasa_interes_global = nueva_tasa
            
# Crea dos cuentas 
cuenta1 = CuentaBancaria("Alice")
cuenta2 = CuentaBancaria("Bob")

# Imprime cuántas cuentas existen a nivel global.
print(f"Total de cuentas creadas: {CuentaBancaria.total_cuentas_creadas}")

# Deposítale 10,000 a cuenta1
cuenta1.depositar(10000)

# Proyecta el interés de cuenta1 con la tasa actual del 5%
cuenta1.proyectar_interes()

# Usa el método de clase para que el Banco suba la tasa de interés a 0.10 (10%).
CuentaBancaria.modificar_tasa_interes(0.10)

# Vuelve a proyectar el interés de cuenta1 para ver cómo la ganancia se duplicó automáticamente.
cuenta1.proyectar_interes()

# Intenta cambiar el nombre de Alice a un texto en blanco `""` para comprobar que el setter la bloquea.
cuenta1.titular = "" 
print(f"Titular actual de cuenta1: {cuenta1.titular}")   
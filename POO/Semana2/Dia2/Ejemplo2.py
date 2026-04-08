class UsuarioBancario:
    def __init__(self, nombre_ingresado, pin_ingresado):
        self.nombre = nombre_ingresado
        # Atributo privado
        self.__pin = pin_ingresado

    # Get tradicional (ventanilla para consultar)
    def get_pin(self):
        return self.__pin

    def set_pin(self, nuevo_pin):
        # Validacion 
        if len(str(nuevo_pin)) == 4:
            self.__pin = nuevo_pin
            print("Operacion exitosa. Pin actualizado.")
        else:
            print("Error: El PIN debe de tener exactamente 4 dígitos.")


# programa principal
print("--- SISTEMA DE SEGURIDAD ---")
cliente = UsuarioBancario("Diego", 1234)

# Primer intento de hackeo: intentar acceder directamente al atributo privado
# print(cliente.__pin) # ERROR, no se puede acceder a un atributo privado desde fuera de la clase

# Segundo intento de hackeo: intentar acceder al atributo privado usando el metodo get
print(cliente.get_pin())

# o opcion 2 guardando el valor del PIN en una variable
pin_cliente = cliente.get_pin() 
print(pin_cliente)

cliente.set_pin(5544) # Operacion exitosa


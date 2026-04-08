class AgenteSeguridad:
    def evaluar_entrada(self):
        print("Bienvenido al Sistema de Seguridad")
        nivel = int(input("Ingrese el nivel de seguridad de la puerta(un número del 1 al 5): "))
        if nivel >= self.nivel_acceso:
            print(f"Acceso concedido para {self.nombre}")
        else:
            print("Acceso denegado")

guardia_turno = AgenteSeguridad()
guardia_turno.nombre = "Juan"
guardia_turno.nivel_acceso = 2

guardia_turno.evaluar_entrada()


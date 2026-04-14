class EmpleadoBase:
    def iniciar_rutina(self):
        print("1. Llego a la oficina a las 8:00 am.")
        print("2. Reviso mis correos electrónicos y mensajes.")
        print("3. Planifico mi día y establezco mis prioridades.")

    def monto_salario(self):
        return 3000

class Programador(EmpleadoBase):
    def iniciar_rutina(self):
        super().iniciar_rutina()
        print("4. Escribo codigo y resyelvo problemas.")
    
    def monto_salario(self):
        return super().monto_salario() + 2000

trabajador1 = Programador()
trabajador1.iniciar_rutina()


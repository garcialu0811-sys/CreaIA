class EmpleadoTienda:
    # Atributos de clase
    sueldo_minimo = 300
    cantida_empleados = 0

    # Constructor
    def __init__(self, nombre, id_empleado):
       # nombre
       self.nombre = nombre
       # id de empleado
       self.id = id_empleado

       # Cada vez que nace un empleado, nodificamos el atributo de clase
       EmpleadoTienda.cantida_empleados += 1
    
    # Metodo de clase(la ley modifica el aumento del salario)
    @classmethod
    def aumento_nacional(cls, nuevo_salario):
        # recordatorio, usar cls y no self en los metodos de clase
        cls.sueldo_minimo = nuevo_salario

        print("\n[COMUNICADO OFICIAL] El gobierno ha cambiado el sueldo minimo")
    
    # Metodo mostrar recibos de pago
    def mostrar_recibos(self):
        # El objeto lee la informacion compartida de su clase y sus datos propios
        print(f"Empleado {self.id}: {self.nombre} | Pago a recibir: {EmpleadoTienda.sueldo_minimo}")
        

# Programa inicial
# Print de encabezado
print("\n -- SISTEMA DE PLANILLA NACIONAL --")

# Creamos 2 personas empleadas
trabajador1 = EmpleadoTienda("Juan", 1)
trabajador2 = EmpleadoTienda("Luis", 2)

# Comprobar que la variable compartida funciono(contador)
print(f"Total de empleados: {EmpleadoTienda.cantida_empleados}")

# Dia de pago
# Generar los recibos de ambos empleados
trabajador1.mostrar_recibos()
trabajador2.mostrar_recibos()

# El gobierno interviene, aumentamos el sueldo minimo
EmpleadoTienda.aumento_nacional(400)

# Siguiente semana de pago
# generar los recibos de ambos empleados
trabajador1.mostrar_recibos()
trabajador2.mostrar_recibos()
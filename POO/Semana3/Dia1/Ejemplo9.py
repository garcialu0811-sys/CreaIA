# =================================================================
#        SISTEMA DE GESTIÓN DE FLOTA - RENT-A-CAR (UNIFICADO)
# =================================================================

# CLASE PADRE: Características físicas y seguridad del vehículo
class Vehiculo:
    def __init__(self, placa, marca, modelo):
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        # Atributo privado para evitar fraudes en el kilometraje
        self.__kilometraje = 0 

    @property
    def kilometraje(self):
        """Getter: Permite consultar el valor privado desde fuera."""
        return self.__kilometraje

    @kilometraje.setter
    def kilometraje(self, nuevo_km):
        """Setter: Filtro de seguridad que previene reducciones fraudulentas."""
        if nuevo_km < self.__kilometraje:
            print(f"[ALERTA FRAUDE]: El kilometraje de {self.placa} no puede disminuir.")
        else:
            self.__kilometraje = nuevo_km

# CLASE HIJO: Lógica de negocio, disponibilidad y tarifas
class AutoAlquiler(Vehiculo):
    # ATRIBUTOS DE CLASE (Compartidos por toda la flota)
    tarifa_diaria = 45.0
    total_disponibles = 0

    def __init__(self, placa, marca, modelo):
        # Inicialización de atributos heredados del padre
        super().__init__(placa, marca, modelo)
        # Estado de disponibilidad individual
        self.disponible = True
        # Aumentamos el conteo global de la flota al registrar un nuevo auto
        AutoAlquiler.total_disponibles += 1

    def gestionar_alquiler(self, dias):
        """Procesa el alquiler y actualiza el inventario global."""
        if self.disponible:
            costo = dias * AutoAlquiler.tarifa_diaria
            self.disponible = False
            # REGLA: Excluir de los disponibles mientras esté rentado
            AutoAlquiler.total_disponibles -= 1
            print(f"--- ALQUILER PROCESADO ---")
            print(f"Vehículo: {self.marca} [{self.placa}] | Total a cobrar: ${costo}")
        else:
            print(f"[ERROR]: El auto {self.placa} no está disponible actualmente.")

    def gestionar_devolucion(self, km_final):
        """Procesa el retorno y suma el vehículo de nuevo a disponibles."""
        if not self.disponible:
            # Actualizamos kilometraje pasando por la validación del padre
            self.kilometraje = km_final  
            self.disponible = True
            # REGLA: Volver a sumar al conteo de disponibles
            AutoAlquiler.total_disponibles += 1
            print(f"--- DEVOLUCIÓN EXITOSA ---")
            print(f"Vehículo {self.placa} devuelto y listo para rentar.")
        else:
            print(f"[AVISO]: El vehículo ya se encontraba en el predio.")

    @classmethod
    def cambiar_tarifa_general(cls, nueva_tarifa):
        """Permite a la gerencia actualizar la tarifa para todos los autos."""
        cls.tarifa_diaria = nueva_tarifa
        print(f"[SISTEMA]: Tarifa actualizada a ${cls.tarifa_diaria} para toda la flota.")

# =================================================================
#                 SIMULACIÓN DEL SISTEMA INTEGRADO
# =================================================================

# 1. Registro de vehículos (Inventario inicial)
carro_1 = AutoAlquiler("P-444ZZZ", "Toyota", "Hilux")
carro_2 = AutoAlquiler("P-111AAA", "Honda", "Civic")

print(f"ESTADO INICIAL: {AutoAlquiler.total_disponibles} vehículos disponibles.")

# 2. Operaciones de Alquiler
print("\n--- Iniciando transacciones ---")
carro_1.gestionar_alquiler(3)
print(f"Disponibles actualmente: {AutoAlquiler.total_disponibles}")

# 3. Devolución y validación de seguridad (Kilometraje)
print("\n--- Proceso de retorno ---")
carro_1.gestionar_devolucion(300)

print("Intentando reducir kilometraje a 50...")
carro_1.kilometraje = 50 # Activará el mensaje de Alerta Fraude del padre

# 4. Cambio de tarifa y nueva renta
print("\n--- Actualización de Gerencia ---")
AutoAlquiler.cambiar_tarifa_general(60.0)
carro_2.gestionar_alquiler(2) # El costo ahora se calcula con la nueva tarifa ($120)

print(f"\nESTADO FINAL DE FLOTA: {AutoAlquiler.total_disponibles} vehículos disponibles.")
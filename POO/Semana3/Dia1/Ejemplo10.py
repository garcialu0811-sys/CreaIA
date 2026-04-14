
# CLASE PADRE: Características físicas del vehículo
class Vehiculo:
    def __init__(self, placa, marca, modelo):
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        # Atributo privado para proteger el kilometraje
        self.__kilometraje = 0 

    @property
    def kilometraje(self):
        """Permite consultar el valor privado."""
        return self.__kilometraje

    # AQUÍ ESTABA EL ERROR: El nombre debe ser igual al de la propiedad
    @kilometraje.setter
    def kilometraje(self, nuevo_km): 
        """Valida que el kilometraje no disminuya (fraude)."""
        if nuevo_km < self.__kilometraje:
            print(f"[ALERTA]: Intento de alteración en {self.placa}. No se actualizó.")
        else:
            self.__kilometraje = nuevo_km

# CLASE HIJO: Lógica de negocio y disponibilidad
class AutoAlquiler(Vehiculo):
    # ATRIBUTOS DE CLASE
    tarifa_diaria = 45.0
    total_disponibles = 0 

    def __init__(self, placa, marca, modelo):
        super().__init__(placa, marca, modelo)
        self.en_alquiler = False
        # Al registrarse, entra como disponible automáticamente
        AutoAlquiler.total_disponibles += 1

    def alquilar_vehiculo(self, dias):
        if self.en_alquiler == False:
            costo = dias * AutoAlquiler.tarifa_diaria
            self.en_alquiler = True
            AutoAlquiler.total_disponibles -= 1
            print(f"--- ALQUILER PROCESADO ---")
            print(f"Vehículo: {self.placa} | Total: ${costo}")
        else:
            print(f"[ERROR]: El vehículo {self.placa} ya está rentado.")

    def devolver_vehiculo(self, km_final):
        if self.en_alquiler == True:
            # Ahora esto sí encontrará el setter correcto
            self.kilometraje = km_final 
            self.en_alquiler = False
            AutoAlquiler.total_disponibles += 1
            print(f"--- DEVOLUCIÓN EXITOSA ---")
            print(f"Vehículo {self.placa} ahora está disponible.")
        else:
            print(f"[AVISO]: El vehículo ya estaba en el predio.")

# 1. Registro inicial
carro_1 = AutoAlquiler("P-100BBB", "Toyota", "Yaris")
carro_2 = AutoAlquiler("P-200CCC", "Hyundai", "Tucson")

print(f"ESTADO INICIAL: {AutoAlquiler.total_disponibles} vehículos disponibles.")

# 2. Alquiler
print("\n--- Rentando 2 vehículos ---")
carro_1.alquilar_vehiculo(5)
carro_2.alquilar_vehiculo(3)
print(f"DISPONIBLES ACTUALMENTE: {AutoAlquiler.total_disponibles}") 

# 3. Devolución (Esto ya no dará error)
print("\n--- Devolviendo 1 vehículo ---")
carro_1.devolver_vehiculo(150)
print(f"DISPONIBLES TRAS DEVOLUCIÓN: {AutoAlquiler.total_disponibles}")
# CLASE PADRE: Características físicas del vehículo
class Vehiculo:
    def __init__(self, placa, marca, modelo):
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        # Atributo privado para proteger el kilometraje [cite: 130, 132]
        self.__kilometraje = 0 

    @property
    def kilometraje(self):
        """Permite consultar el valor privado."""
        return self.__kilometraje

    @kilometraje.setter
    def presion(self, nuevo_km): # Nota: Se usa la lógica de validación de presión [cite: 131, 150]
        """Valida que el kilometraje no disminuya (fraude)."""
        if nuevo_km < self.__kilometraje:
            print(f"[ALERTA]: Intento de alteración en {self.placa}.")
        else:
            self.__kilometraje = nuevo_km

# CLASE HIJO: Lógica de negocio y disponibilidad
class AutoAlquiler(Vehiculo):
    # ATRIBUTOS DE CLASE (Compartidos) [cite: 134, 135]
    tarifa_diaria = 45.0
    total_disponibles = 0 # Este contador manejará la flota real

    def __init__(self, placa, marca, modelo):
        # Inicializa datos del padre [cite: 144, 145]
        super().__init__(placa, marca, modelo)
        self.en_alquiler = False
        # Al registrarse, entra como disponible automáticamente
        AutoAlquiler.total_disponibles += 1

    def alquilar_vehiculo(self, dias):
        """Resta del inventario global si está disponible."""
        if self.en_alquiler == False:
            costo = dias * AutoAlquiler.tarifa_diaria
            self.en_alquiler = True
            # REGLA: Excluir de los disponibles al alquilar
            AutoAlquiler.total_disponibles -= 1
            print(f"--- ALQUILER PROCESADO ---")
            print(f"Vehículo: {self.placa} | Total: ${costo}")
        else:
            print(f"[ERROR]: El vehículo {self.placa} ya está rentado.")

    def devolver_vehiculo(self, km_final):
        """Suma al inventario global al ser devuelto."""
        if self.en_alquiler == True:
            self.kilometraje = km_final # Actualiza km con validación
            self.en_alquiler = False
            # REGLA: Sumar a disponibles al regresar a la flota
            AutoAlquiler.total_disponibles += 1
            print(f"--- DEVOLUCIÓN EXITOSA ---")
            print(f"Vehículo {self.placa} ahora está disponible.")
        else:
            print(f"[AVISO]: El vehículo ya estaba en el predio.")


# 1. Registro inicial (Aparecen como disponibles)
carro_1 = AutoAlquiler("P-100BBB", "Toyota", "Yaris")
carro_2 = AutoAlquiler("P-200CCC", "Hyundai", "Tucson")
carro_3 = AutoAlquiler("P-300DDD", "Kia", "Sportage")

print(f"ESTADO INICIAL: {AutoAlquiler.total_disponibles} vehículos disponibles.")

# 2. Salida de vehículos (Alquiler)
print("\n--- Rentando 2 vehículos ---")
carro_1.alquilar_vehiculo(5)
carro_2.alquilar_vehiculo(3)

# Aquí se excluyen los que están en alquiler
print(f"DISPONIBLES ACTUALMENTE: {AutoAlquiler.total_disponibles}") 

# 3. Regreso de vehículo (Devolución)
print("\n--- Devolviendo 1 vehículo ---")
carro_1.devolver_vehiculo(150)

# Al ser devuelto, se suma de nuevo
print(f"DISPONIBLES TRAS DEVOLUCIÓN: {AutoAlquiler.total_disponibles}")
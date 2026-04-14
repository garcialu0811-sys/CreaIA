
class Vehiculo:
    def __init__(self, placa, marca, modelo):
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        # Atributo privado para evitar fraudes
        self.__kilometraje = 0 

    @property
    def kilometraje(self):
        return self.__kilometraje

    @kilometraje.setter
    def kilometraje(self, nuevo_km):
        # Lógica para prevenir reducción fraudulenta
        if nuevo_km < self.__kilometraje:
            print(f"[ALERTA FRAUDE]: El kilometraje de {self.placa} no puede disminuir.")
        else:
            self.__kilometraje = nuevo_km

class AutoAlquiler(Vehiculo):
    # ATRIBUTOS DE CLASE
    tarifa_diaria = 45.0
    total_disponibles = 0

    def __init__(self, placa, marca, modelo):
        # Llamamos al constructor del padre
        super().__init__(placa, marca, modelo)
        self.disponible = True
        # Aumentamos el conteo global de la flota
        AutoAlquiler.total_disponibles += 1

    def gestionar_alquiler(self, dias):
        if self.disponible:
            costo = dias * AutoAlquiler.tarifa_diaria
            self.disponible = False
            AutoAlquiler.total_disponibles -= 1
            print(f"Alquiler de {self.marca} exitoso. Total a cobrar: ${costo}")
        else:
            print(f"El auto {self.placa} no está disponible.")

    def gestionar_devolucion(self, km_final):
        self.kilometraje = km_final  # Se valida en el padre
        self.disponible = True
        AutoAlquiler.total_disponibles += 1
        print(f"Vehículo {self.placa} devuelto a la flota.")

    @classmethod
    def cambiar_tarifa_general(cls, nueva_tarifa):
        cls.tarifa_diaria = nueva_tarifa
        print(f"[SISTEMA]: Tarifa actualizada a ${cls.tarifa_diaria} para toda la flota.")


# 1. Registro de vehículos
carro_1 = AutoAlquiler("P-444ZZZ", "Toyota", "Hilux")
carro_2 = AutoAlquiler("P-111AAA", "Honda", "Civic")

print(f"Autos listos para rentar: {AutoAlquiler.total_disponibles}")

# 2. Alquiler y prevención de fraude
carro_1.gestionar_alquiler(3)
carro_1.gestionar_devolucion(300)

print("\nIntentando bajar el kilometraje a 50...")
carro_1.kilometraje = 50 # Esto disparará la validación del padre

# 3. Actualización de tarifa por gerencia
AutoAlquiler.cambiar_tarifa_general(60.0)
carro_2.gestionar_alquiler(2) # El costo ahora se calcula con 60
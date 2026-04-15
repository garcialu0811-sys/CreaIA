from abc import ABC,  abstractmethod

class VehiculoComercial(ABC):
    @property
    @abstractmethod
    def tarifa_km(self):
        pass

    def calcular_viaje(self, kilometro):
        total = kilometro * self.tarifa_km
        print(f"Costo del viaje: {total}")

class Taxi(VehiculoComercial):
    @property
    def tarifa_km(self):
        return 500

mi_taxi = Taxi()
mi_taxi.calcular_viaje(10) # 10 * 500 = 5000
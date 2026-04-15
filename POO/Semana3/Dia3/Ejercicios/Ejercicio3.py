from abc import ABC, abstractmethod

class VehiculoTerrestre(ABC):
    @abstractmethod
    def conducir_ruedas(self):
        pass

class VehiculoAcuatico(ABC):
    @abstractmethod
    def encender_helices(self):
        pass

class VehiculoAnfibio(VehiculoTerrestre, VehiculoAcuatico):
    def conducir_ruedas(self):
        print("[VEHICULO ANFIBIO] Activando tracción 4x4 en terreno rocoso.")

    def encender_helices(self):
        print("[VEHICULO ANFIBIO] Retrayendo ruedas y activando propulsión acuática")

class AutoComun(VehiculoTerrestre):
    def conducir_ruedas(self):
        print("[VEHICULO] Conduciendo auto")

class Lancha(VehiculoAcuatico):
    def encender_helices(self):
        print("[LANCHA] Helices encendidas")

print("\n==== AUTO ====")
auto = AutoComun()
auto.conducir_ruedas()

print("\n==== LANCHA ====")
lancha = Lancha()
lancha.encender_helices()

print("\n==== ANFIBIO ====")
anfibio = VehiculoAnfibio()
anfibio.conducir_ruedas()
anfibio.encender_helices()

print("\n==== RUTA TERRESTRE ====")
ruta_terrestre = [auto, anfibio]

for lista in ruta_terrestre:
    lista.conducir_ruedas()

print("\n==== RUTA ACUATICA ====")
ruta_acuatica = [lancha, anfibio]

for lista in ruta_acuatica:
    lista.encender_helices()
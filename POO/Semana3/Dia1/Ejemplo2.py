# La superclase (el padre)
class Vehiculo:
    def encender_motor(self):
        print("[SISTEMA] | El motor se ha encendido.")

    def apagar_motor(self):
        print("[SISTEMA] | El motor se ha apagado.")

# Subclase 1(hijo)
class Auto(Vehiculo):
    def encender_aire(self):
        print("[AUTO] | Aire acondicionado esta encendido.")

# Subclase 2(hijo)
class Moto(Vehiculo):
    def hacer_acrobacias(self):
        print("[MOTO] | Levantando la rueda delantera.")

carro = Auto()
moto = Moto()

print("=== Auto ===")
print("Acciones del Auto:")
carro.encender_motor()  # Método heredado de Vehiculo (El padre)
carro.encender_aire()    # Método específico de Auto (El hijo)
carro.apagar_motor()   # Método heredado de Vehiculo (El padre)

print("\n=== Moto ===")
print("Acciones de la Moto:")
moto.encender_motor()   # Método heredado de Vehiculo (El padre)
moto.hacer_acrobacias()  # Método específico de Moto (El hijo)

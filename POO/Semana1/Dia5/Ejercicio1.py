# ==========================================   
#               Ejercicio 1
#          Ejercicio Integrador
#   Centro de Control de Drones "SkyWatch"
# ==========================================   

class DronVigilancia:
    def __init__(self, nombre, modelo):
        self.nombre = nombre
        self.modelo = modelo
        self.bateria = 100
        self.estado_de_vuelo = "En Tierra"

    def despegue(self):
        if self.bateria >= 25:
            self.estado_de_vuelo = "En Vuelo"
            print(f"¡Despegue exitoso! El dron {self.nombre} ahora está en el aire.")
        else:
            print(f"[ERROR: Batería insuficiente ({self.bateria}%). Requiere al menos 25%].")
    
    def patrullaje(self):
        if self.estado_de_vuelo == "En Vuelo":
            self.bateria = self.bateria - 30
            print(f"Patrullaje completado. Consumo: 30%. Batería restante: {self.bateria}%.")
            
            if self.bateria <= 10:
                self.estado_de_vuelo = "En Tierra"
                print("¡ALERTA! Batería en nivel crítico. Aterrizaje automático realizado.")
        else:
            print("[ERROR: El dron no puede patrullar si aún está en tierra].")

    def recarga(self):
        if self.estado_de_vuelo == "En Tierra":
            self.bateria = 100
            print("Recarga completa. Batería al 100%.")
        else:
            print("[ERROR: No se puede recargar en pleno vuelo. ¡Peligro de caída!]")

    def mostrar_estado(self):
        print(f"\n --- ESTADO ACTUAL: {self.nombre} [{self.modelo}] ---")
        print(f"Batería: {self.bateria}% | Estado: {self.estado_de_vuelo}")

print(">>> INICIANDO SISTEMA SKYWATCH <<<")
nombre_dron = input("Ingrese nombre del dron: ")
modelo_dron = input("Ingrese modelo del dron: ")
mi_dron = DronVigilancia(nombre_dron, modelo_dron)

opcion = ""
while opcion != 4:
    mi_dron.mostrar_estado()
    opcion = input("\n¿Qué accion desea realizar? (1. Despegar / 2. Patrullar / 3. Recargar / 4. Salir): ")

    match opcion:
        case "1":
           mi_dron.despegue() 
        case "2":
            mi_dron.patrullaje()
        case "3":
            mi_dron.recarga()
        case "4":
            print("Apagando el Sistema...")
            break
        case _:
            print("[ERROR: Selecciona una opción válida].")


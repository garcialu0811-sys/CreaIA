class DronVigilancia:
    def __init__(self, nombre, modelo):
        # El constructor recibe nombre y modelo externamente [cite: 11, 12]
        self.nombre = nombre
        self.modelo = modelo
        # Atributos por defecto al salir de fábrica [cite: 13]
        self.bateria = 100
        self.estado_vuelo = "En Tierra"

    def despegar(self):
        # Solo despega si tiene al menos 25% de batería [cite: 18]
        if self.bateria >= 25:
            self.estado_vuelo = "En Vuelo"
            print(f"¡Despegue exitoso! El dron ahora está en el aire.")
        else:
            print(f"[ERROR: Batería insuficiente ({self.bateria}%). Requiere al menos 25%].")

    def patrullar(self):
        # Solo patrulla si ya está en el aire [cite: 20]
        if self.estado_vuelo == "En Vuelo":
            self.bateria -= 30
            print(f"Patrullaje completado. Consumo: 30%. Batería restante: {self.bateria}%.")
            
            # Aterrizaje automático por seguridad [cite: 22, 23]
            if self.bateria < 10:
                self.estado_vuelo = "En Tierra"
                print("¡ALERTA! Batería en nivel crítico. Aterrizaje automático realizado.")
        else:
            print("[ERROR: El dron no puede patrullar si aún está en tierra].")

    def recargar(self):
        # Debe estar en tierra para recargar [cite: 24]
        if self.estado_vuelo == "En Tierra":
            self.bateria = 100
            print("Recarga completa. Batería al 100%.")
        else:
            print("[ERROR: No se puede recargar en pleno vuelo. ¡Peligro de caída!]")

    def mostrar_estado(self):
        print(f"\nESTADO ACTUAL: {self.nombre} [{self.modelo}]")
        print(f"Batería: {self.bateria}% | Estado: {self.estado_vuelo}")

# --- Programa Principal ---
print(">>> INICIANDO SISTEMA SKYWATCH <<<")
nombre_u = input("Ingrese nombre del dron: ")
modelo_u = input("Ingrese modelo del dron: ")
mi_dron = DronVigilancia(nombre_u, modelo_u)

opcion = ""
while opcion != "4":
    mi_dron.mostrar_estado()
    print("¿Qué acción desea realizar? (1. Despegar / 2. Patrullar / 3. Recargar / 4. Salir): ")
    opcion = input("Selección: ")

    if opcion == "1":
        mi_dron.despegar()
    elif opcion == "2":
        mi_dron.patrullar()
    elif opcion == "3":
        mi_dron.recargar()
    elif opcion == "4":
        print("Apagando el Sistema...")
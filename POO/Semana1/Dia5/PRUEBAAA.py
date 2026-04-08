class DrongVigilancia:
    def __init__(self, nombre, modelo):
        self.nombre = nombre
        self.modelo = modelo
        self.bateria = 100
        self.estado_dron = 'En Tierra'

    def despegue(self):
        if self.bateria >= 25:
            self.estado_dron = 'En vuelo'
            print('\nDespegue exitoso! El dron ahora esta en el aire.')
        
        else:
            print('\nERROR: La bateria es insuficiente para que el dron pueda despegar.')

    def patrullaje(self):
        if self.estado_de_vuelo == "En Vuelo":
            self.bateria = self.bateria - 30
            print(f"Patrullaje completado. Consumo: 30%. Batería restante: {self.bateria}%.")
            
            if self.bateria <= 10:
                self.estado_de_vuelo = 'En Tierra'
                print("¡ALERTA! Batería en nivel crítico. Aterrizaje automático realizado.")
        else:
            print("[ERROR: El dron no puede patrullar si aún está en tierra].")

    def recargar(self):
        if self.estado_dron == 'En Tierra':
            self.bateria = 100
            print('Recarga completada. Bateria al 100')
        else:
            print('\nERROR: El dron no se puede recargar si se encuentra en vuelo')
      
    def mostrar_estado(self):
        print(f'\n--- ESTADO ACTUAL: {self.nombre} [{self.modelo}] ---')
        print(f'Bateria: {self.bateria} | Estado: {self.estado_dron}')

print('\n>>> INICIANDO SISTEMA SKYWATCH <<<')
nombre = input('\nIngrese el nombre del dron: ')
modelo = input('Ingrese el modelo del dron: ')
dron = DrongVigilancia(nombre, modelo)

while True:
    dron.mostrar_estado()
    print('\nQue accion desea realizar?: \n1. Despegar \n2. Patrullar \n3. Recargar \n4. Apagar')
    opcion = input('Seleccione una opcion: ')
    match opcion:
        case '1':
            dron.despegue()
        case '2':
            dron.patrullaje()
        case '3':
            dron.recargar()
        case '4':
            print('Apagando el sistema...')
            break
        case _:
            print('ERROR: Seleccione una opcion valida.')
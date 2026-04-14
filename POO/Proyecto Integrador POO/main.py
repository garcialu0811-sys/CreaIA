# Definimos la clase POKEMON 
class Pokemon:
    def __init__(self, nombre, hp_maximo, energia_maxima):
        self.nombre = nombre
        self.hp_maximo = hp_maximo
        self. energia_maxima = energia_maxima
        self.__hp_actual = 100
        self.__energia_actual = 100
    
    @property
    def hp_actual(self):
        return self.__hp_actual
    
    @hp_actual.setter
    def hp_actual(self):
        pass

    @property
    def energia_actual(self):
        return self.__energia_actual

    @energia_actual.setter
    def energia_actual(self):
        pass


print("="*60)
print(f'{"SIMULADOR DE BATALLAS POKÉMON (POO)":^60}')
print("="*60)
print("Seleccione el Modo de Juego:")
print("1. Jugador vs Jugador")
print("2. Jugador vs Computadora")
opcion = int(input("> Opción: "))

while True:
    print("="*60)
    print(f'{"CATALOGO POKÉMON OFICIAL":^60}')
    print("="*60)
    

    match opcion:
        case "1":
            pass
        case "2":
            pass
        case _:
            print("Opcion invalida")
    print("Seleccione el Modo de Juego:")
class TermostatoDigital:
    def __init__(self):
        self.__temperatura = 20
    
    @property
    def temperatura(self):
        return self.__temperatura
    
    @temperatura.setter
    def temperatura(self, nueva_temperatura):

        nueva_temperatura = input("Ajuste la temperatura: ")
        self.__temperatura = nueva_temperatura
        print("Temperatura ajustada")

    # Consulta la temperatura, imprime la temperatural actual en pantalla
    def consultar(self):
        print(f"El estado de la temperatura es: {self.__temperatura}")
    
        


print("--- TERMOSTATO DIGITAL ---")
print("1. Consultar temperatura")
print("2. Ajustar temperatura")
opcion = input("Seleccione una opcion: ")
temperatura1 = TermostatoDigital()

while True:
    match opcion:
        case "1":
            temperatura1.consultar()
        case "2":
            temperatura1.temperatura
        case _:
            print("[ERROR: Selecciona una opción válida].")

    opcion = input("Seleccione un opcion: ")
    

class Temperatura:
    def __init__(self):
        self.__grados = 20
    
    @property
    def grados(self):
        return self.__grados
    
    @grados.setter
    def grados(self, nuevo_grado):
        if nuevo_grado < 0:
            print("Temperatura invalida")
        else:
            self.__grados = nuevo_grado
    
clima = Temperatura()
# Con el metodo tradicional, necesitamos usar el clima.get_grados() para obtener el valor de grados
# clima.__grados No funciona

print(clima.grados)
clima.grados = 50
print(clima.grados)

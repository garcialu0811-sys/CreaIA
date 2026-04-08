# La tarjeta de puntos VIP
# * Crea la clase llamada "TarjetaVIP"
# 2. dentro de la clase, crea un metodo llamado mostrar_puntos() 
#    que imprima: "sus puntos acumulados son: {puntos del objeto}"
# 3. crea un segundo metodo llamado sumar_puntos(), que le sume 50 
#    puntos al atributo del objeto e imprima "se han sumado 50 puntos por su compra"
# 4. fuera de la clase (en el programa principal), instancia un objeto llamado tarjeta_carlos.
# 5. asignele un atributo puntos con el valor inicial de 100
# 6. llama al metodo para mostrar los puntos, luego llama al metodo 
#    para sumar, y finalmente vuelve a mostrar los puntos para comprobar que la matematica funcionó

class TarjetaVIP:
    def mostrar_puntos(self):
        print(f"Sus puntos acumulados son: {self.puntos}")
        
    def sumar_puntos(self):
        self.puntos += 50
        print(f"Se han sumado 50 puntos por su compra.")

tarjeta_clase = TarjetaVIP()
tarjeta_clase.puntos = 100

tarjeta_clase.mostrar_puntos()
tarjeta_clase.sumar_puntos()
tarjeta_clase.mostrar_puntos()

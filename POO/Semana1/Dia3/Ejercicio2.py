
# ## Reto Único Integrador: El Personaje de Videojuego
# * **Instrucción:** Vas a programar la lógica del jugador para un videojuego de rol (RPG).
#     1. Crea la clase `Personaje`.
#     2. Crea el método `__init__`. Este debe pedir como parámetro externo el `nombre` del personaje.
#     3. Dentro del `__init__`, asígnale los siguientes atributos por defecto (sin pedirlos en los paréntesis):
#         * `self.nivel = 1`
#         * `self.puntos_de_vida = 100`
#         * `self.esta_vivo = True`
# imprimir: "[nombre] recibió daño. Vida restante: [puntos_de_vida]".
#     5. Fuera de la clase, instancia a tu personaje dándole un nombre. 
#     6. Atácalo dos veces usando el método `recibir_dano` (ej: pásale 40 de daño, y luego 70 de daño) para comprobar que su estado cambia de vivo a muerto.

class Personaje:
    def __init__(self, nombre):
        self.nivel = 1
        self.puntos_de_vida =100
        self.esta_vivo = True
        self.nombre = nombre

    def recibir_dano(self, cantidad_dano):
        self.puntos_de_vida -= cantidad_dano
        if self.puntos_de_vida <= 0:
            if self.esta_vivo == True:
                self.esta_vivo = False
                print(f"¡{self.nombre} ha sido derrotado!")
        else:
            print(f"{self.nombre} recibio daño. Vida restante: {self.puntos_de_vida}.")

personaje1 = Personaje("Juan")
personaje1.recibir_dano(40)
personaje1.recibir_dano(70)

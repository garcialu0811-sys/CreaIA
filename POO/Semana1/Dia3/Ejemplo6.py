class Personaje:
    def __init__(self, nombre):
        self.nombre = nombre
        # Atributos internos por defecto (no se piden al usuario)
        self.nivel = 1
        self.puntos_de_vida = 100
        self.esta_vivo = True

    def recibir_dano(self, cantidad_dano):
        # Validamos primero si el personaje ya está derrotado
        if not self.esta_vivo:
            print(f"{self.nombre} ya está derrotado, no puedes hacerle más daño.")
            return # Termina la ejecución del método aquí

        # Restamos la vida
        self.puntos_de_vida -= cantidad_dano
        
        # Evaluamos si sobrevivió al ataque
        if self.puntos_de_vida <= 0:
            self.puntos_de_vida = 0 # Evitamos vidas negativas
            self.esta_vivo = False
            print(f"¡{self.nombre} ha recibido un golpe letal y ha sido derrotado!")
        else:
            print(f"{self.nombre} recibió {cantidad_dano} de daño. Vida restante: {self.puntos_de_vida}")

# 1. Creación del personaje
heroe = Personaje("Arthur")
print(f"El héroe {heroe.nombre} de nivel {heroe.nivel} ha entrado a la arena con {heroe.puntos_de_vida} HP.")

# 2. Simulador de combate
print("\n--- ¡Inicia el combate! ---")
heroe.recibir_dano(40)
heroe.recibir_dano(70)

# 3. Comprobación final
print("\nEstado final del héroe:")
print(f"¿Está vivo?: {heroe.esta_vivo}")
print(f"Vida actual: {heroe.puntos_de_vida}")


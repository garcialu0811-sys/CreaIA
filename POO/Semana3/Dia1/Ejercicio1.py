class PersonajeBase:
    def caminar(self):
        print("[PERSONAJE] | El personaje está avanzando por el mapa.")

    def descansar(self):
        print("[PERSONAJE] | El personaje está recuperando energía.\n")
    
class Mago(PersonajeBase):
    def lanzar_hechizo(self):
        print("[MAGO] | ¡El Mago lanza una bola de fuego!")

class Guerrero(PersonajeBase):
    def bloquear_ataque(self):
        print("[GUERRERO] | ¡El guerrero levanta su escudo de metal!.")


mi_mago = Mago()
mi_guerrero = Guerrero()
print(f'{"=== MAGO ===":=^55}')
print(f'{"Acciones del Mago:":^55}')
mi_mago.caminar()  
mi_mago.lanzar_hechizo() 
mi_mago.descansar() 

print(f'{"=== GUERRERO ===":=^55}')
print(f'{"Acciones del Guerrero:":^55}')
mi_guerrero.caminar()  
mi_guerrero.bloquear_ataque() 
mi_guerrero.descansar()


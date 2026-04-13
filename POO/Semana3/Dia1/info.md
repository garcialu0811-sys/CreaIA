# Herencia básica

## Principio DRY(Don't Repeat Yourself | No te repitas)

### Micro Ejemplo
```py
class Perro:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def comer(self):
        print("Comiendo....")

class Gato:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def comer(self):
        print("Comiendo....")
```

### Solucion usando herencia

```py
# 1. El padre
class Animal:
    def comer(self):
        print("El animal esta comiendo")

# 2. El hijo (hereda del padre usando parentesis)

class Perro(Animal):
    pass

# 3. Uso
mi_mascota = Perro()
mi_mascora.comer()

```
---
### Agregando habilidades exclusivas al hijo
```py
# La superclase (el padre)
class Vehiculo:
    def encender_motor(self):
        print("[SISTEMA] | El motor se ha encendido.")

    def apagar_motor(self):
        print("[SISTEMA] | El motor se ha apagado.")

# Subclase 1(hijo)
class Auto(Vehiculo):
    def encender_aire(self):
        print("[AUTO] | Aire acondicionado esta encendido.")

# Subclase 2(hijo)
class Moto(Vehiculo):
    def hacer_acrobacias(self):
        print("[MOTO] | Levantando la rueda delantera.")

carro = Auto()
moto = Moto()

print("=== Auto ===")
print("Acciones del Auto:")
carro.encender_motor()  # Método heredado de Vehiculo (El padre)
carro.encender_aire()    # Método específico de Auto (El hijo)
carro.apagar_motor()   # Método heredado de Vehiculo (El padre)

print("\n=== Moto ===")
print("Acciones de la Moto:")
moto.encender_motor()   # Método heredado de Vehiculo (El padre)
moto.hacer_acrobacias()  # Método específico de Moto (El hijo)
```

### Ejercicio Practico: Heroes con Habilidades Únicas
```py
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
```

## Constructor del hijo
```py
class Padre:
    def __init__(self, apellido):
        self.apellido = apellido

class Hijo(Padre):
    def __init(self, nombre): # ¡Peligro! Esto borra el __init__ de la clase Padre
        self.nombre = nombre

chico = Hijo("Carlos")
#print(chico.apellido) # ERROR!!! el hijo nunca recibio el paellido porque su _init__ aplasto al padre
```

### Solucion
`super()`. Significa literalmente "Superclase" o "Padre". Dentro del `__init__` del hijo, llamamos a `super().__init()` y le pasamos los ingredientes que le corresponden al padre.

```py

```

### Ejercicio

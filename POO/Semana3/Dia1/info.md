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
```py
```

# Las muchas formas (Polimorfismo)
**SOLID**:
1. **S - Single Responsability (Responsabilidad Única):**

2. **O - Open7close (Abierto y Cerrado):**

3. **L - Liskov Substitution (Sustitución de Liskov):**

4. **I - Interface Segregation (Segregación de Interfaces):**

5. **D - Dependecy Inversion (Inversion de Dependencias):**


```py
class EmpleadoDios:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def calcular_impuestos(self):
        return self.salario * 0.13

```

### SOlUCION

```py
# 1. Responsabilidad: solo almacenar datos del empleado
class Empleano
    def __init__(self, nombre, salario):
            self.nombre = nombre
            self.salario = salario

# 2. Responsabilidad: Solo hacer calculos financieros
class CalculadoraFinanciera:
    def calcular_impuestos(self, empleado):
        return empleado.salario * 0.13

# 3. Responsabilidad: Solo maneja el almacenamiento
class RepositorioBaseDeDatos:
    def guardar(self, empleado):
        print(f"Conectando al servidos.... GUardando a {empleado.nombre}")
```

## La Rebelion del Hijo (Sobrescritura de Métodos)
```py
class PersonaMayor:
    def saludar(self):
        print("Buenas tardes estimado, cómo se encuentra usted eldía de hoy, es un placer saludarlo.")
    
class Adolecente(PersonaMayor):
    def saludar(self):
        print("Hola, todo bien?")

senor = PersonaMayor()
chico = Adolecente()

senor.saludar()
chico.saludar() 
```

### el poder del polimorfismo
perros, gatos y vacas, y quiere que todos hagan un sonido, escribiría algo asi:
    `if tipo == "perro": ladrar()`
    `elif tipo == "gatos": maullar()`

### Ejemplo | Simulacion de granja
```py
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def __str__(self):
        return f"Animal: {self.nombre}"
    
    def hacer_sonido(self):
        print(f"{self.nombre} hace un sonido genérico.")

class Perro(Animal):
    def hacer_sonido(self):
        print(f"{self.nombre} | El perro hace: Guau, Guauuuu")
    
class Gato(Animal):
    def hacer_sonido(self):
        print(f"{self.nombre} | El gato hace: Miau, Miauuu")

class Pato(Animal):
    def hacer_sonido(self):
        print(f"{self.nombre} | El pato hace: Cuac, Cuac")

animal1 = Perro("Peludo")
animal2 = Gato("Pelusa")
animal3 = Pato("Pancho")

lista_granja  =[animal1, animal2]
lista_granja.append(animal3)

animal_desconocido = Animal("Extraterrestre")

lista_granja.append(animal_desconocido)

print(animal1)

for animal in lista_granja:
    animal.hacer_sonido()

for animal in lista_granja:
    print(animal)
```

## Combinando lo viejo y lo nuevo
### 1. Usar `super()`en métodos normales

```py
class EmpleadoBase:
    def iniciar_rutina(self):
        print("1. Llego a la oficina a las 8:00 am.")
        print("2. Reviso mis correos electrónicos y mensajes.")
        print("3. Planifico mi día y establezco mis prioridades.")

    def monto_salario(self):
        return 3000

class Programador(EmpleadoBase):
    def iniciar_rutina(self):
        super().iniciar_rutina()
        print("4. Escribo codigo y resyelvo problemas.")
    
    def monto_salario(self):
        return super().monto_salario() + 2000

trabajador1 = Programador()
trabajador1.iniciar_rutina()
```

## El gran devate: Herencia vs. Polimorfismo


## escenario1: Herencia SIN Polimorfismo
## escenario2: Polimorfismo SIN Herencia


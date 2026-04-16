# Repaso
- 

# try - except
```py
valor1 = 10
valor2 = 0

try:
    # Ingreso una "a" en lugar de un número, lo que generará una 
    dato = int(input("Ingrese un número: "))
    resueltado = valor1 / valor2
    print(resultado)

except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")

except ValueError:
    print("Error: Por favor, ingrese un número válido")

except (ZeroDivisionError, ValueError) as error:
    print(f"Error: {error}")

except Exception:
    print(f"Error genral: Ocurrio un error inesperado.")
```

# "Es un" vs "Tiene un" ( La composicion basica)

*la regla de oro del diseño de software es:
    * si la realcion es "Es un"(Un perro "es un" Animal), usamos Herencia
    * Si la relacion es "tiene un" (Un perro "tiene un" Collar) usamos Composicion

```py
# Pieza (objeto independiente)
class Motor:
    def __init__(self, caballos_fuerza):
        self.caballos = caballos_fuerza
        self.endendido = False

    def arrancar(self):
        self.encendido = True
        print("Encendiendo el motor")

# El contenedor (guarda la pieza en su interior)
class Auto:
    def __init__(self, marca, modelo, potencia_motor):
        self.marca = marca
        self.modelo = modelo

        self.corazon_mecanico = Motor(potencia_motor)

    def encender_auto(self):
        print("Girando la llave para encender...")

        self.corazon_mecanico.arrancar()

mi_carro = Auto("Toyota", "Corolla", 200)
mi_carro.encender_auto()
```

## Inyeccion de Piezas( Objetos como Párametros)

# Inyeccion de dependencias
```py
class Procesador:
    def __init__(self, modelo):
        self.modelo = modelo

class TarjetaVideo:
    def __init__(self, memoria_gb):
        self.memoria = memoria_gb

class Computadora:
    def __init__(self, cpu_externa, gpu_externa):
        self.cpu = cpu_externa
        self.gpu = gpu_externa
    
    def mostrar_especificaciones(self):
        print("\nEspecificaciones del equipo: ")

        # Accedemos a los atributos de las piezas inyectadas
        print(f"- Procesador: {self.cpu.modelo}")
        print(f"- Gráficos: {self.gpu.memoria} GB de video")

# Fabricar las piezas por separado
intel_i9 = Procesador("Intel Core i9 14900K")
nvidia_x = TarjetaVideo(24)

pc_gamer = Computadora(intel_i9, nvidia_x)
pc_gamer.mostrar_especificaciones()
```

## Relaciones "1 a Muchos" (Listas de Objetos)
```py
class Estudiante:
    def __init__(self, nombre, carnet):
        self.nombre = nombre
        self.carnet = carnet 

class Curso:
    def __init__(self, nombre_curso):
        self.nombre_curso = nombre_curso

        self.lista_matriculados = []

    def matricular(self, nuevo_estudiante):
        self.lista_matriculados.append(nuevo_estudiante)

        print(f"Sistema: {nuevo_estudiante.nombre} matriculado con éxito")

    def pasar_lista(self):
        for alumno in self.lista_matriculados:
            print(f"- {alumno.carnet}: {alumno.nombre}")

alumno1 = Estudiante("Luis", "A001")
alumno2 = Estudiante("Keyla", "A002")

curso_poo = Curso("POO")

curso_poo.matricular(alumno1)
curso_poo.matricular(alumno2)

curso_poo.pasar_lista()

curso_poo.lista_matriculados[0].nombre = "Luis Fernando"

curso_poo.pasar_lista()
```


### Ejercicio integrador: 
Actúan como Ingenieros desarrollando un sistema de Biblioteca. 
* **Instrucciones del Ejercicio:**
    1. Creen la clase `Libro`.
        * Constructor: Recibe `titulo` y `autor`.
        * Método `__str__`: Debe retornar el texto `"{titulo}" escrito por {autor}`.
    2. Creen la clase `Biblioteca`.
        * Constructor: Recibe el `nombre_sucursal`. Inicializa un atributo `self.catalogo` como una lista vacía.
        * Método `agregar_libro(self, nuevo_libro)`: Usa `append` para meter el libro al catálogo.
        * Método `mostrar_inventario(self)`: Debe imprimir el nombre de la sucursal y luego usar un bucle `for` para recorrer el catálogo. Dentro del `for`, simplemente hagan un `print(libro)`. Gracias al `__str__` que programaron antes, Python imprimirá los datos bonitos automáticamente.
    3. **Programa Principal:**
        * Instancien 3 libros distintos.
        * Instancien una Biblioteca.
        * Agreguen los 3 libros a la biblioteca usando el método.
        * Llamen a `mostrar_inventario()`.

```py
class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def __str__(self):
        return f"{self.titulo} escrito por {self.autor}"
    
class Biblioteca:
    def __init__(self, nombre_sucursal):
        self.nombre_sucursal = nombre_sucursal
        self.catalogo = []
    
    def agregar_libro(self, nuevo_libro):
        self.catalogo.append(nuevo_libro)

    def mostrar_inventario(self):
        print(f"Sucursal: {self.nombre_sucursal}")

        for libro in self.catalogo:
            print(f"- {libro}")

libro1 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes")
libro2 = Libro("Cien años de soledad", "Gabriel García Márquez")
libro3 = Libro("Orgullo y prejuicio", "Jane Austen")

biblioteca1 = Biblioteca("Quetzaltenango")

biblioteca1.agregar_libro(libro1)
biblioteca1.agregar_libro(libro2)
biblioteca1.agregar_libro(libro3)

biblioteca1.mostrar_inventario()

```
# Ejercicio integrador: 
# Actúan como Ingenieros desarrollando un sistema de Biblioteca. 
#  **Instrucciones del Ejercicio:**
#     1. Creen la clase `Libro`.
#         * Constructor: Recibe `titulo` y `autor`.
#         * Método `__str__`: Debe retornar el texto `"{titulo}" escrito por {autor}`.
#     2. Creen la clase `Biblioteca`.
#         * Constructor: Recibe el `nombre_sucursal`. Inicializa un atributo `self.catalogo` como una lista vacía.
#         * Método `agregar_libro(self, nuevo_libro)`: Usa `append` para meter el libro al catálogo.
#         * Método `mostrar_inventario(self)`: Debe imprimir el nombre de la sucursal y luego usar un bucle `for` para recorrer el catálogo. Dentro del `for`, simplemente hagan un `print(libro)`. Gracias al `__str__` que programaron antes, Python imprimirá los datos bonitos automáticamente.
#     3. **Programa Principal:**
#         * Instancien 3 libros distintos.
#         * Instancien una Biblioteca.
#         * Agreguen los 3 libros a la biblioteca usando el método.
#         * Llamen a `mostrar_inventario()`.

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

biblioteca1 = Biblioteca(" Biblioteca Nacional de Guatemala ")

biblioteca1.agregar_libro(libro1)
biblioteca1.agregar_libro(libro2)
biblioteca1.agregar_libro(libro3)

biblioteca1.mostrar_inventario()


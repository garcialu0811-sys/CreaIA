# Modelo
class Libro:
    def __init__(self, titulo, autor, id_libro):
        self.titulo = titulo
        self.autor = autor
        self.id_libro = id_libro
        self.prestado = False

    def marcar_como_prestado(self):
        if not self.prestado:
            self.prestado = True
            return True
        return False
    
class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def buscar_por_id(self, id_libro):
        for libro in self.libros:
            if libro.id_libro == id_libro:
                return libro

# VISTA
class VistaBiblioteca:
    @staticmethod
    def mostrar_menu():
        print("\n --- SISTEMA DE BIBLIOTECA --- ")
        print("1. Añadir Libro")
        print("2. Listar Libros")
        print("3. Prestar Libro")
        print("4. Salir")

        return input("Seleccione una opción: ")
    
    @staticmethod
    
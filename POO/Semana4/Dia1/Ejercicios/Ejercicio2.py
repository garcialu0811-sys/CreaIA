# --- MODELO (Lógica de datos y reglas de negocio) ---
class Libro:
    def __init__(self, titulo, autor, id_libro):
        self.titulo = titulo
        self.autor = autor
        self.id_libro = id_libro
        self.prestado = False  # Estado inicial: Disponible

    def marcar_como_prestado(self):
        """Cambia el estado del libro. No usa print."""
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
        return None


# --- VISTA (Interfaz de usuario) ---
class VistaBiblioteca:
    @staticmethod
    def mostrar_menu():
        print("\n--- SISTEMA DE BIBLIOTECA ---")
        print("1. Añadir Libro")
        print("2. Listar Libros")
        print("3. Prestar Libro")
        print("4. Salir")
        return input("Seleccione una opción: ")

    @staticmethod
    def pedir_datos_libro():
        titulo = input("Título del libro: ")
        autor = input("Autor: ")
        id_libro = input("ID único: ")
        return titulo, autor, id_libro

    @staticmethod
    def pedir_id_prestamo():
        return input("Ingrese el ID del libro a prestar: ")

    @staticmethod
    def mostrar_tabla_libros(libros):
        print("\n{:<10} {:<20} {:<20} {:<10}".format("ID", "Título", "Autor", "Estado"))
        print("-" * 60)
        for libro in libros:
            estado = "Prestado" if libro.prestado else "Disponible"
            print("{:<10} {:<20} {:<20} {:<10}".format(
                libro.id_libro, libro.titulo, libro.autor, estado
            ))

    @staticmethod
    def mostrar_mensaje(mensaje):
        print(f">> {mensaje}")


# --- CONTROLADOR (Cerebro del programa) ---
class ControladorBiblioteca:
    def __init__(self):
        self.modelo_biblioteca = Biblioteca()
        self.vista = VistaBiblioteca()

    def ejecutar(self):
        while True:
            opcion = self.vista.mostrar_menu()

            if opcion == "1":
                # Añadir Libro
                titulo, autor, id_libro = self.vista.pedir_datos_libro()
                nuevo_libro = Libro(titulo, autor, id_libro)
                self.modelo_biblioteca.agregar_libro(nuevo_libro)
                self.vista.mostrar_mensaje("Libro registrado con éxito.")

            elif opcion == "2":
                # Listar Libros
                libros = self.modelo_biblioteca.libros
                self.vista.mostrar_tabla_libros(libros)

            elif opcion == "3":
                # Prestar Libro
                id_a_buscar = self.vista.pedir_id_prestamo()
                libro = self.modelo_biblioteca.buscar_por_id(id_a_buscar)
                
                if libro:
                    if libro.marcar_como_prestado():
                        self.vista.mostrar_mensaje(f"El libro '{libro.titulo}' ha sido prestado.")
                    else:
                        self.vista.mostrar_mensaje("Error: El libro ya está prestado.")
                else:
                    self.vista.mostrar_mensaje("Error: Libro no encontrado.")

            elif opcion == "4":
                self.vista.mostrar_mensaje("Cerrando aplicación...")
                break
            else:
                self.vista.mostrar_mensaje("Opción no válida.")


# --- INICIO DE LA APLICACIÓN ---
if __name__ == "__main__":
    app = ControladorBiblioteca()
    app.ejecutar()
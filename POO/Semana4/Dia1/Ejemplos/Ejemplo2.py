# MODELO (Logica pura)
class ModeloTarea:
    def __init__(self, descripcion):
        self.descripcion = descripcion
        self.completada = False

# VISTA
class VistaTarea:
    @staticmethod
    def mostrar_menu():
        print("\n 1. Agregar Tarea\n 2. Mostrar Tareas \n 3.Salir")
        return input("Opcion: ")

    @staticmethod
    def mostrar_lista(lista):
        print("\nLista de tareas: ")

        for tarea in lista:
            estado = "Completada" if tarea.completada else "Pendiente"
            print(f"{tarea.descripcion} está en estado: {estado}")
    
    @staticmethod
    def solicitar_descripcion():
        return input("Descripcion de la tarea: ")
    
    @staticmethod
    def mostrar_mensaje(mensaje):
        print(mensaje)

# CONTROLADOR
class ControladorTareas:
    def __init__(self):
        self.tareas = []
        self.vista = VistaTarea()

    def ejecutar(self):
        while True:
            opcion = self.vista.mostrar_menu()
            if opcion == "1":
                descripcion = self.vista.solicitar_descripcion()
                tarea = ModeloTarea(descripcion)
                self.tareas.append(tarea)
            elif opcion == "2":
                self.vista.mostrar_lista(self.tareas)
            elif opcion == "3":
                self.vista.mostrar_mensaje("Saliendo...")
                break


# Inicio del programa
if __name__ == "__main__":
    controlador = ControladorTareas()
    controlador.ejecutar()
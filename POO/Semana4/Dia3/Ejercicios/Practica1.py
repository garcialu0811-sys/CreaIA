from abc import ABC, abstractmethod

class EnergiaInvalidaError(Exception):
    pass

class Nucleo:
    def __init__(self, id_unico):
        self.id_entidad = id_unico

class EntidadBase(ABC):
    def __init__(self, nombre_id, energia_inicial):
        # --- CORRECCIÓN DE INDENTACIÓN ---
        if energia_inicial < 0:
            raise EnergiaInvalidaError("La energia inicial no puede ser un valor negativo.")
        
        # Estas líneas deben estar FUERA del if para que se ejecuten siempre que NO haya error
        self.energia_actual = energia_inicial
        self.nucleo_vital = Nucleo(nombre_id)
    
    @abstractmethod
    def alimentarse(self, cantidad_energia=10):
        pass

    def __add__(self, otra_entidad):
        return self.energia_actual + otra_entidad.energia_actual

class Sintetizador(EntidadBase):
    def alimentarse(self, cantidad_energia=10):
        self.energia_actual += cantidad_energia
        print(f"Sintetizador {self.nucleo_vital.id_entidad} absorbió luz ambiental. Energía: {self.energia_actual}")

class Consumidor(EntidadBase):
    def alimentarse(self, cantidad_energia=10):
        ganancia = cantidad_energia // 2
        self.energia_actual += ganancia
        print(f"Consumidor {self.nucleo_vital.id_entidad} consumió recursos. Energía: {self.energia_actual}")

# Herencia Múltiple
class Hibrido(Sintetizador, Consumidor):
    def __init__(self, nombre_id, energia_inicial):
        # super() se encarga de llamar a los constructores necesarios
        super().__init__(nombre_id, energia_inicial)
    
    def alimentarse(self, cantidad_energia=10):
        self.energia_actual += (cantidad_energia + 5)
        print(f"Híbrido {self.nucleo_vital.id_entidad} activó modo de alimentación dual. Energía: {self.energia_actual}")

def iniciar_ciclo_vital(lista_de_entidades):
    print("\n--- INICIANDO PROCESO DE ALIMENTACIÓN DE LA COLONIA ---")
    for entidad in lista_de_entidades:
        entidad.alimentarse()

def ejecutar_laboratorio():
    colonia_digital = []
    print("\n--- SISTEMA DE GESTIÓN DE ENERGÍAS ---")

    while True:
        print("\nMenú de Control: ")
        print("1. Crear nuevo Sintetizador")
        print("2. Crear nuevo Híbrido")
        print("3. Ejecutar ciclo vital (Alimentar a todos)")
        print("4. Mostrar energía total de la colonia")
        print("5. Salir")

        seleccion = input("Seleccione una opción: ")

        if seleccion == "5":
            print("Cerrando simulación del ecosistema.")
            break
        
        if seleccion in ["1", "2"]:
            try:
                nombre_id = input("Asigne un nombre/ID a la entidad: ")
                lectura_energia = input("Ingrese el nivel de energía inicial: ")
                puntos_energia = int(lectura_energia)

                if seleccion == "1":
                    nueva_entidad = Sintetizador(nombre_id, puntos_energia)
                else:
                    nueva_entidad = Hibrido(nombre_id, puntos_energia)

                colonia_digital.append(nueva_entidad)
                print(f"Entidad '{nombre_id}' registrada con éxito")
            
            except ValueError:
                print("Error de Entrada: Debe ingresar un número entero para la energía.")
            except EnergiaInvalidaError as error_negativo:
                print(f"Error de Validación: {error_negativo}")
        
        elif seleccion == "3":
            if not colonia_digital:
                print("Aviso: No hay entidades en la colonia para alimentar.")
            else:
                iniciar_ciclo_vital(colonia_digital)
        
        elif seleccion == "4":
            if len(colonia_digital) < 1:
                print("La colonia no tiene energía porque no existen entidades.")
            elif len(colonia_digital) == 1:
                # Corregido: antes intentabas sumar si solo había una, ahora solo mostramos el valor único
                print(f"Energía única de {colonia_digital[0].nucleo_vital.id_entidad}: {colonia_digital[0].energia_actual}")
            else:
                total_dos_primeras = colonia_digital[0] + colonia_digital[1]
                print(f"Suma de energía de las dos primeras entidades: {total_dos_primeras}")

                total_acumulado = 0
                for entidad_actual in colonia_digital:
                    total_acumulado = total_acumulado + entidad_actual.energia_actual
                
                print(f"Energía total de toda la colonia ({len(colonia_digital)} entes): {total_acumulado}")
        else:
            # Una pequeña corrección para que el "Opción no válida" no salga siempre
            if seleccion not in ["1", "2", "3", "4", "5"]:
                print("Opción no válida")

if __name__ == "__main__":
    ejecutar_laboratorio()
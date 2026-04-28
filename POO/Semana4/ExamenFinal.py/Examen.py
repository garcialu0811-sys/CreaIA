from abc import ABC, abstractmethod

class NucleoEnergia:
    def __init__(self):
        self.estado = "Operacional"

    def consumir(self, cantidad, nivel_actual):
        nuevo_nivel = nivel_actual - cantidad
        if nuevo_nivel < 0:
            return 0
        else:
            return nuevo_nivel

class NaveEspacial(ABC):

    contador_naves = 0 

    def __init__(self, nombre, registro, energia):
        self.nombre = nombre
        self.registro = registro
        self._energia = energia  
        self._escudos = 100     
        self.estado = "Activo"
        
        self.nucleo = NucleoEnergia()
        
        NaveEspacial._incrementar_contador()

    @classmethod
    def _incrementar_contador(cls):
        """Método de clase para gestionar el conteo histórico de naves."""
        cls.contador_naves += 1

    # --- 3. ENCAPSULAMIENTO (Uso de Decoradores) ---
    @property
    def energia(self):
        """Permite leer el nivel de energía de forma controlada."""
        return self._energia

    @energia.setter
    def energia(self, valor):
        """Valida que la energía siempre esté en el rango de 0 a 100."""
        if valor >= 0 and valor <= 100:
            self._energia = valor
        else:
            print("Error: El nivel de energía debe estar entre 0 y 100.")

    @property
    def escudos(self):
        """Permite consultar el estado de los escudos."""
        return self._escudos

    @escudos.setter
    def escudos(self, valor):
        """Lógica de integridad: si el escudo es 0, la nave es vulnerable."""
        if valor < 0:
            self._escudos = 0
        elif valor > 100:
            self._escudos = 100
        else:
            self._escudos = valor
            
        # Si los escudos fallan, el estado cambia automáticamente
        if self._escudos == 0:
            self.estado = "Vulnerable"

    @abstractmethod
    def mision_especializada(self):
        """Método abstracto: obliga a las hijas a definir su propia misión."""
        pass

    # --- 4. DUNDER METHODS (Métodos Especiales) ---
    def __str__(self):
        """Define cómo se imprime la nave elegantemente como texto."""
        return f"[{self.registro}] {self.nombre} - Energía: {self._energia}% - Estado: {self.estado}"

    def __lt__(self, otra):
        """Sobrecarga del operador '<' para comparar naves por su energía."""
        return self._energia < otra.energia

# --- RAMAS DE HERENCIA ---

class NaveCombate(NaveEspacial):
    def __init__(self, nombre, registro, energia, potencia_fuego):
        # super() llama al constructor de la clase padre (NaveEspacial)
        super().__init__(nombre, registro, energia)
        self.potencia_fuego = potencia_fuego

    def mision_especializada(self):
        """Implementación propia de combate."""
        return f"Atacando con potencia de {self.potencia_fuego}."

class NaveCarga(NaveEspacial):
    def __init__(self, nombre, codigo_registro, nivel_energia, capacidad):
        super().__init__(nombre, codigo_registro, nivel_energia)
        self.capacidad = capacidad

    def mision_especializada(self):
        """Implementación propia de transporte."""
        return f"Transportando {self.capacidad} toneladas métricas."

    def __add__(self, otra):
        """Sobrecarga del operador '+': permite fusionar dos naves de carga."""
        if isinstance(otra, NaveCarga):
            nueva_capacidad = self.capacidad + otra.capacidad
            # Retorna una nueva nave con la suma de capacidades
            return NaveCarga(f"Fusión-{self.nombre}", "FUSION-99", 100, nueva_capacidad)
        raise ValueError("Solo se pueden fusionar naves de carga.")

# --- 1. HERENCIA MÚLTIPLE ---
class InterceptorHibrido(NaveCombate, NaveCarga):
    def __init__(self, nombre, registro, energia, potencia, capacidad):
        # Inicialización manual para asegurar que la clase base se configure bien
        NaveEspacial.__init__(self, nombre, registro, energia)
        self.potencia_fuego = potencia
        self.capacidad = capacidad

    def mision_especializada(self):
        """Demuestra el polimorfismo al combinar habilidades de ambas ramas."""
        return f"Misión Versátil: Combate ({self.potencia_fuego}) y Carga ({self.capacidad})."

# --- RELACIONES Y LISTAS ---
class EstacionEspacial:
    def __init__(self, nombre):
        self.nombre = nombre
        self.hangar = []  # Lista que almacena los objetos de tipo Nave

    def inyectar_nave(self, nave):
        """Agrega una nave ya construida a la colección del hangar."""
        self.hangar.append(nave)

# --- 5. INTERFAZ Y RESILIENCIA (Manejo de Errores) ---
def ejecutar_estacion():
    aethelgard = EstacionEspacial("Aethelgard")
    
    while True:
        print(f"\n--- ESTACIÓN GALÁCTICA {aethelgard.nombre} ---")
        print("1. Registrar Nave")
        print("2. Realizar Misión")
        print("3. Ver Flota")
        print("4. Salir")
        
        try:
            opcion = input("Seleccione una acción: ")
            
            if opcion == "1":
                tipo = input("Tipo (1.Combate, 2.Carga, 3.Híbrida): ")
                nom = input("Nombre de la nave: ")
                reg = input("Código de registro: ")
                
                if tipo == "1":
                    aethelgard.inyectar_nave(NaveCombate(nom, reg, 100, 50))
                elif tipo == "2":
                    aethelgard.inyectar_nave(NaveCarga(nom, reg, 100, 200))
                elif tipo == "3":
                    aethelgard.inyectar_nave(InterceptorHibrido(nom, reg, 100, 80, 150))
                print(">>> Nave registrada exitosamente.")

            elif opcion == "2":
                # Verificamos si el hangar tiene naves antes de operar
                if len(aethelgard.hangar) == 0:
                    print("No hay naves disponibles en el hangar.")
                    continue
                
                idx = int(input("Índice de la nave en el hangar (0, 1...): "))
                gasto = int(input("Cantidad de energía para la misión: "))
                
                if gasto < 0:
                    print("Error: No se puede consumir energía negativa.")
                else:
                    nave = aethelgard.hangar[idx]
                    # Validación lógica de negocio: tener suficiente energía
                    if nave.energia < gasto:
                        print("¡ADVERTENCIA! Energía insuficiente para despegar.")
                    else:
                        # Se usa el componente Nucleo para el cálculo
                        nueva_e = nave.nucleo.consumir(gasto, nave.energia)
                        nave.energia = nueva_e # El setter valida el valor
                        print(f"Éxito: {nave.mision_especializada()}")

            elif opcion == "3":
                print("\n=== ESTADO DE LA FLOTA ACTUAL ===")
                # enumerate() nos da el índice y el objeto al mismo tiempo
                for i, n in enumerate(aethelgard.hangar):
                    print(f"{i}. {n}") # Imprime el objeto usando su método __str__

            elif opcion == "4":
                print("Desconectando sistemas de Aethelgard... Adiós.")
                break

        # Captura de errores para evitar que el programa se cierre
        except ValueError:
            print("ERROR: La entrada debe ser un número entero.")
        except IndexError:
            print("ERROR: El índice seleccionado no existe en el hangar.")
        except Exception as e:
            print(f"ALERTA: Ha ocurrido un error inesperado: {e}")

# Punto de entrada del programa
if __name__ == "__main__":
    ejecutar_estacion()
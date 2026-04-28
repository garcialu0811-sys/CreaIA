from abc import ABC, abstractmethod

# --- 2. COMPOSICIÓN (10% de la rúbrica) ---
class NucleoEnergia:
    """
    Gestiona el componente físico de energía de la nave. 
    Se instancia dentro del constructor de la NaveEspacial.
    """
    def __init__(self):
        self.estado_sistema = "Operacional"

    def calcular_consumo(self, cantidad_a_gastar, energia_actual):
        """Lógica para restar energía asegurando que no sea menor a cero."""
        resultado_final = energia_actual - cantidad_a_gastar
        if resultado_final < 0:
            return 0
        else:
            return resultado_final

# --- 1. ARQUITECTURA ABSTRACTA (10% de la rúbrica) ---
class NaveEspacial(ABC):
    """
    Clase base abstracta que define el ADN de la flota.
    """
    # Lógica de Clase (5%): Atributo global para conteo histórico
    total_naves_fabricadas = 0 

    def __init__(self, nombre_vehiculo, codigo_registro, nivel_energia_inicial):
        self.nombre_vehiculo = nombre_vehiculo
        self.codigo_registro = codigo_registro
        # --- 3. ENCAPSULAMIENTO (15%): Atributos privados ---
        self._nivel_combustible = nivel_energia_inicial
        self._estado_escudos = 100
        self.estado_operativo = "Activo"
        
        # Composición: El objeto se crea internamente al fabricar la nave
        self.componente_nucleo = NucleoEnergia()
        
        # Uso de método de clase para actualizar el contador global
        NaveEspacial.registrar_nueva_nave()

    @classmethod
    def registrar_nueva_nave(cls):
        """Incrementa el contador histórico de la estación."""
        cls.total_naves_fabricadas += 1

    # --- SETTERS Y GETTERS CON VALIDACIÓN (Encapsulamiento) ---
    @property
    def combustible(self):
        return self._nivel_combustible

    @combustible.setter
    def combustible(self, nuevo_valor):
        """Valida que el combustible esté en el rango 0-100%."""
        if nuevo_valor >= 0 and nuevo_valor <= 100:
            self._nivel_combustible = nuevo_valor
        else:
            print("Alerta: Valor de combustible fuera de rango galáctico.")

    @property
    def escudos(self):
        return self._estado_escudos

    @escudos.setter
    def escudos(self, valor_impacto):
        """Si los escudos llegan a 0, la nave cambia a estado Vulnerable."""
        if valor_impacto < 0:
            self._estado_escudos = 0
        elif valor_impacto > 100:
            self._estado_escudos = 100
        else:
            self._estado_escudos = valor_impacto
            
        if self._estado_escudos == 0:
            self.estado_operativo = "Vulnerable"

    @abstractmethod
    def ejecutar_mision_especializada(self):
        """Obliga a las clases hijas a implementar su comportamiento único."""
        pass

    # --- 4. DUNDER METHODS (15% de la rúbrica) ---
    def __str__(self):
        """Presentación elegante de la nave al ser consultada."""
        return f"Nave: {self.nombre_vehiculo} | Registro: {self.codigo_registro} | Energía: {self._nivel_combustible}%"

    def __lt__(self, otra_nave):
        """Compara naves basándose en su nivel de energía actual."""
        return self._nivel_combustible < otra_nave.combustible

# --- JERARQUÍA Y HERENCIA (15% de la rúbrica) ---

class NaveCombate(NaveEspacial):
    def __init__(self, nombre, codigo, energia, potencia_fuego):
        super().__init__(nombre, codigo, energia)
        self.potencia_fuego = potencia_fuego

    def ejecutar_mision_especializada(self):
        return f"Abriendo fuego con potencia de {self.potencia_fuego} megajoules."

class NaveCarga(NaveEspacial):
    def __init__(self, nombre, codigo, energia, capacidad_maxima):
        super().__init__(nombre, codigo, energia)
        self.capacidad_maxima = capacidad_maxima

    def ejecutar_mision_especializada(self):
        return f"Transportando {self.capacidad_maxima} toneladas de suministros."

    def __add__(self, otra_nave):
        """Dunder Method: Fusiona dos naves de carga sumando sus capacidades."""
        if isinstance(otra_nave, NaveCarga):
            nueva_capacidad = self.capacidad_maxima + otra_nave.capacidad_maxima
            nombre_fusion = f"Fusión-{self.nombre_vehiculo}"
            return NaveCarga(nombre_fusion, "SUMA-XP", 100, nueva_capacidad)
        raise ValueError("La fusión solo es posible entre naves de carga.")

# HERENCIA MÚLTIPLE (Parte de Jerarquía y Herencia)
class InterceptorHibrido(NaveCombate, NaveCarga):
    def __init__(self, nombre, codigo, energia, potencia, capacidad):
        # Inicialización manual para evitar ambigüedades en herencia múltiple
        NaveEspacial.__init__(self, nombre, codigo, energia)
        self.potencia_fuego = potencia
        self.capacidad_maxima = capacidad

    def ejecutar_mision_especializada(self):
        return f"Iniciando protocolo híbrido: Ataque ({self.potencia_fuego}) y Carga ({self.capacidad_maxima})."

# --- RELACIONES Y LISTAS (10% de la rúbrica) ---
class EstacionAethelgard:
    def __init__(self):
        self.nombre_estacion = "Aethelgard"
        self.lista_naves_activas = [] # Gestión de flota mediante lista

    def inyectar_nave_al_hangar(self, objeto_nave):
        """Agrega naves fabricadas a la colección de la estación."""
        self.lista_naves_activas.append(objeto_nave)

# --- MANEJO DE ERRORES E INTERFAZ (15% de la rúbrica) ---
def iniciar_consola_mision():
    centro_mando = EstacionAethelgard()
    
    while True:
        print(f"\n=== SISTEMA DE MISIÓN CRÍTICA: {centro_mando.nombre_estacion} ===")
        print("1. Registrar Nave")
        print("2. Ejecutar Misión")
        print("3. Comparar Energías")
        print("4. Mostrar Flota")
        print("5. Salir")
        
        try:
            opcion_usuario = input("\nSeleccione acción: ")
            
            if opcion_usuario == "1":
                print("\nTipos: 1-Combate | 2-Carga | 3-Híbrida")
                tipo_clase = input("Seleccione tipo: ")
                nombre = input("Nombre del vehículo: ")
                codigo = input("Código alfanumérico: ")
                
                if tipo_clase == "1":
                    nueva = NaveCombate(nombre, codigo, 100, 75)
                elif tipo_clase == "2":
                    nueva = NaveCarga(nombre, codigo, 100, 500)
                elif tipo_clase == "3":
                    nueva = InterceptorHibrido(nombre, codigo, 100, 90, 250)
                else:
                    print("Tipo no reconocido.")
                    continue
                
                centro_mando.inyectar_nave_al_hangar(nueva)
                print(f">>> Éxito. Total histórico fabricado: {NaveEspacial.total_naves_fabricadas}")

            elif opcion_usuario == "2":
                # Verificamos si hay naves disponibles
                if len(centro_mando.lista_naves_activas) == 0:
                    print("El hangar está vacío.")
                    continue
                
                indice = int(input("Índice de la nave a operar (0, 1, 2...): "))
                energia_mision = int(input("Energía requerida para la misión: "))
                
                nave_seleccionada = centro_mando.lista_naves_activas[indice]
                
                if energia_mision < 0:
                    print("Error: No se puede consumir energía negativa.")
                elif nave_seleccionada.combustible < energia_mision:
                    print("Operación cancelada: Energía insuficiente.")
                else:
                    # Uso de lógica del componente NucleoEnergia
                    nuevo_nivel = nave_seleccionada.componente_nucleo.calcular_consumo(energia_mision, nave_seleccionada.combustible)
                    # El setter de combustible valida el valor
                    nave_seleccionada.combustible = nuevo_nivel
                    print(f"Resultado: {nave_seleccionada.ejecutar_mision_especializada()}")

            elif opcion_usuario == "3":
                # Comparación usando el método dunder __lt__
                if len(centro_mando.lista_naves_activas) < 2:
                    print("Se requieren al menos 2 naves para realizar una comparación.")
                    continue
                
                n1 = centro_mando.lista_naves_activas[0]
                n2 = centro_mando.lista_naves_activas[1]
                
                if n1 < n2:
                    print(f"{n1.nombre_vehiculo} tiene menos energía disponible que {n2.nombre_vehiculo}.")
                else:
                    print(f"{n1.nombre_vehiculo} tiene igual o mayor energía que {n2.nombre_vehiculo}.")

            elif opcion_usuario == "4":
                print("\n--- REPORTE DE FLOTA ACTUAL ---")
                if len(centro_mando.lista_naves_activas) == 0:
                    print("No hay naves en el hangar.")
                else:
                    # Cambio: Uso de contador manual para evitar enumerate()
                    posicion_en_hangar = 0
                    for nave in centro_mando.lista_naves_activas:
                        print(f"ID {posicion_en_hangar}: {nave}")
                        posicion_en_hangar = posicion_en_hangar + 1

            elif opcion_usuario == "5":
                print("Desactivando sistemas... Protocolo de cierre finalizado.")
                break

        # Captura de errores para garantizar la resiliencia del sistema
        except ValueError:
            print("ADVERTENCIA: Por favor, ingrese un número entero válido.")
        except IndexError:
            print("ADVERTENCIA: El índice de nave proporcionado no existe en el hangar.")
        except Exception as error_inesperado:
            print(f"FALLO CRÍTICO DEL SISTEMA: {error_inesperado}")

if __name__ == "__main__":
    iniciar_consola_mision()
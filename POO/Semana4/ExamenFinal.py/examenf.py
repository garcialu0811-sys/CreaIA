from abc import ABC, abstractmethod

# --- 2. COMPOSICIÓN (10% de la rúbrica) ---
class NucleoEnergia:
    def __init__(self):
        self.estado_sistema = "Operacional"

    def calcular_consumo(self, cantidad_a_gastar, energia_actual):
        resultado_final = energia_actual - cantidad_a_gastar
        if resultado_final < 0:
            return 0
        else:
            return resultado_final

# --- 1. ARQUITECTURA ABSTRACTA (10% de la rúbrica) ---
class NaveEspacial(ABC):
    total_naves_fabricadas = 0 

    def __init__(self, nombre_vehiculo, codigo_registro, nivel_energia_inicial):
        self.nombre_vehiculo = nombre_vehiculo
        self.codigo_registro = codigo_registro
        # --- 3. ENCAPSULAMIENTO (15%) ---
        self._nivel_combustible = nivel_energia_inicial
        self._estado_escudos = 100
        self.estado_operativo = "Activo"
        self.componente_nucleo = NucleoEnergia()
        NaveEspacial.registrar_nueva_nave()

    @classmethod
    def registrar_nueva_nave(cls):
        cls.total_naves_fabricadas += 1

    @property
    def combustible(self):
        return self._nivel_combustible

    @combustible.setter
    def combustible(self, nuevo_valor):
        if nuevo_valor >= 0 and nuevo_valor <= 100:
            self._nivel_combustible = nuevo_valor
        else:
            print("Alerta: Valor fuera de rango.")

    @abstractmethod
    def ejecutar_mision_especializada(self):
        pass

    # --- 4. DUNDER METHODS (15%) ---
    def __str__(self):
        return f"Nave: {self.nombre_vehiculo} | Registro: {self.codigo_registro} | Energía: {self._nivel_combustible}%"

    def __lt__(self, otra_nave):
        return self._nivel_combustible < otra_nave.combustible

# --- JERARQUÍA Y HERENCIA ---

class NaveCombate(NaveEspacial):
    def __init__(self, nombre, codigo, energia, potencia_fuego):
        super().__init__(nombre, codigo, energia)
        self.potencia_fuego = potencia_fuego

    def ejecutar_mision_especializada(self):
        return f"Abriendo fuego con potencia de {self.potencia_fuego}."

class NaveCarga(NaveEspacial):
    def __init__(self, nombre, codigo, energia, capacidad_maxima):
        super().__init__(nombre, codigo, energia)
        self.capacidad_maxima = capacidad_maxima

    def ejecutar_mision_especializada(self):
        return f"Transportando {self.capacidad_maxima} toneladas."

    def __add__(self, otra_nave):
        if isinstance(otra_nave, NaveCarga):
            nueva_capacidad = self.capacidad_maxima + otra_nave.capacidad_maxima
            return NaveCarga(f"Fusión-{self.nombre_vehiculo}", "FUS-99", 100, nueva_capacidad)
        raise ValueError("Solo se fusionan naves de carga.")

class InterceptorHibrido(NaveCombate, NaveCarga):
    def __init__(self, nombre, codigo, energia, potencia, capacidad):
        NaveEspacial.__init__(self, nombre, codigo, energia)
        self.potencia_fuego = potencia
        self.capacidad_maxima = capacidad

    def ejecutar_mision_especializada(self):
        return f"Protocolo Híbrido: Ataque ({self.potencia_fuego}) y Carga ({self.capacidad_maxima})."

class EstacionAethelgard:
    def __init__(self):
        self.lista_naves_activas = []

    def inyectar_nave(self, objeto_nave):
        self.lista_naves_activas.append(objeto_nave)

# --- MENÚ Y LÓGICA DE CONSOLA ---
def iniciar_consola_mision():
    centro_mando = EstacionAethelgard()
    
    while True:
        # Menú exacto a la imagen solicitada
        print(f"\n>>> ESTACIÓN AETHELGARD ACTIVADA <<<")
        print("1. Registrar | 2. Misión | 3. Comparar | 4. Fusionar | 5. Mostrar flota | 6. Salir")
        
        try:
            opcion = input("Seleccione acción: ")
            
            if opcion == "1":
                print("Tipo (1.Combate, 2.Carga, 3.Híbrida): ", end="")
                tipo = input()
                nombre = input("Nombre: ")
                codigo = input("Código: ")
                
                if tipo == "1":
                    potencia = int(input("Potencia: "))
                    nueva = NaveCombate(nombre, codigo, 100, potencia)
                elif tipo == "2":
                    capacidad = int(input("Capacidad: "))
                    nueva = NaveCarga(nombre, codigo, 100, capacidad)
                elif tipo == "3":
                    potencia = int(input("Potencia: "))
                    capacidad = int(input("Capacidad: "))
                    nueva = InterceptorHibrido(nombre, codigo, 100, potencia, capacidad)
                else:
                    print("Tipo no válido.")
                    continue
                
                centro_mando.inyectar_nave(nueva)
                print(f"Éxito. Total naves fabricadas: {NaveEspacial.total_naves_fabricadas}")

            elif opcion == "2":
                if not centro_mando.lista_naves_activas:
                    print("No hay naves.")
                    continue
                idx = int(input("Índice de nave: "))
                gasto = int(input("Energía a consumir: "))
                nave = centro_mando.lista_naves_activas[idx]
                
                if nave.combustible < gasto:
                    print("Energía insuficiente.")
                else:
                    nuevo_nivel = nave.componente_nucleo.calcular_consumo(gasto, nave.combustible)
                    nave.combustible = nuevo_nivel
                    print(f"Resultado: {nave.ejecutar_mision_especializada()}")

            elif opcion == "3":
                if len(centro_mando.lista_naves_activas) < 2:
                    print("Faltan naves para comparar.")
                    continue
                n1 = centro_mando.lista_naves_activas[0]
                n2 = centro_mando.lista_naves_activas[1]
                if n1 < n2:
                    print(f"{n1.nombre_vehiculo} tiene menos energía que {n2.nombre_vehiculo}")
                else:
                    print(f"{n1.nombre_vehiculo} tiene igual o más energía.")

            elif opcion == "4":
                # Lógica para fusionar naves de carga (__add__)
                print("Seleccione dos naves de carga para fusionar:")
                idx1 = int(input("Índice nave 1: "))
                idx2 = int(input("Índice nave 2: "))
                nave1 = centro_mando.lista_naves_activas[idx1]
                nave2 = centro_mando.lista_naves_activas[idx2]
                
                nueva_fusion = nave1 + nave2
                centro_mando.inyectar_nave(nueva_fusion)
                print(f"Fusión exitosa: {nueva_fusion.nombre_vehiculo}")

            elif opcion == "5":
                print("\n--- REPORTE DE FLOTA ---")
                pos = 0
                for nave in centro_mando.lista_naves_activas:
                    print(f"ID {pos}: {nave}")
                    pos += 1

            elif opcion == "6":
                print("Cerrando sistema...")
                break

        except ValueError:
            print("Error: Ingrese números válidos.")
        except IndexError:
            print("Error: Índice no existe.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    iniciar_consola_mision()
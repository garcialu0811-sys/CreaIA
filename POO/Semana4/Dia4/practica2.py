import json
from abc import ABC, abstractmethod

# ==========================================
# 1. EL MODELO (modelo)
# ==========================================
class FuenteEnergia(ABC):
    def __init__(self, id_generador, capacidad_maxima):
        self.id_generador = id_generador
        self.capacidad_maxima = capacidad_maxima
        self.produccion_actual = 0.0

    @abstractmethod
    def generar(self, condiciones):
        pass

    @abstractmethod
    def obtener_dato_recurso(self):
        """Método para evitar usar hasattr en la vista"""
        pass

class PanelSolar(FuenteEnergia):
    def generar(self, clima):
        # Usamos .strip() como solicitaste para limpiar espacios
        # Comparamos directamente con el texto esperado
        if clima.strip() == "Soleado":
            self.produccion_actual = self.capacidad_maxima
        else:
            self.produccion_actual = 0.0
        return self.produccion_actual

    def obtener_dato_recurso(self):
        return "N/A"

class TurbinaEolica(FuenteEnergia):
    def generar(self, velocidad_viento):
        # Reemplazamos min() por un if tradicional
        velocidad_numerica = float(velocidad_viento)
        eficiencia = velocidad_numerica / 15.0
        
        if eficiencia > 1.0:
            eficiencia = 1.0
            
        self.produccion_actual = self.capacidad_maxima * eficiencia
        return self.produccion_actual

    def obtener_dato_recurso(self):
        return "Viento"

class GeneradorDiesel(FuenteEnergia):
    def __init__(self, id_generador, capacidad_maxima, combustible):
        super().__init__(id_generador, capacidad_maxima)
        self.combustible_disponible = float(combustible)

    def generar(self, litros_a_usar):
        cantidad_solicitada = float(litros_a_usar)
        if self.combustible_disponible >= cantidad_solicitada:
            self.combustible_disponible -= cantidad_solicitada
            self.produccion_actual = self.capacidad_maxima
        else:
            self.produccion_actual = 0.0
        return self.produccion_actual

    def obtener_dato_recurso(self):
        return f"{self.combustible_disponible:.1f}L"

# ==========================================
# 2. LA FABRICA (fabrica)
# ==========================================
class FabricaEnergia:
    _catalogo_clases = {
        "solar": PanelSolar,
        "eolica": TurbinaEolica,
        "diesel": GeneradorDiesel
    }

    @staticmethod
    def crear_fuente(datos_configuracion):
        # Reemplazamos .get() por acceso directo mediante llave
        tipo_energia = datos_configuracion["tipo"]
        
        if tipo_energia == "solar":
            return PanelSolar(
                id_generador=datos_configuracion["id_generador"],
                capacidad_maxima=datos_configuracion["capacidad_maxima"]
            )
        elif tipo_energia == "eolica":
            return TurbinaEolica(
                id_generador=datos_configuracion["id_generador"],
                capacidad_maxima=datos_configuracion["capacidad_maxima"]
            )
        elif tipo_energia == "diesel":
            return GeneradorDiesel(
                id_generador=datos_configuracion["id_generador"],
                capacidad_maxima=datos_configuracion["capacidad_maxima"],
                combustible=datos_configuracion["combustible"]
            )
        else:
            raise ValueError("Tipo de energía no reconocido.")

# ==========================================
# 3. LA VISTA (vista)
# ==========================================
class InterfazRed:
    def mostrar_tablero(self, lista_fuentes):
        ancho_interno = 60
        print("\n╔" + "═" * (ancho_interno + 2) + "╗")
        print(f"║ { 'ESTADO DE LA RED ELÉCTRICA SMART-CITY':^60} ║")
        print("╠" + "═" * (ancho_interno + 2) + "╣")
        print(f"║ {'ID':^10} | {'TIPO':^12} | {'ESTADO/RECURSO':^15} | {'PRODUCCIÓN':^14} ║")
        print("╟" + "─" * (ancho_interno + 2) + "╢")
        
        for fuente in lista_fuentes:
            tipo_nombre = "Desconocido"
            if isinstance(fuente, PanelSolar): tipo_nombre = "Solar"
            elif isinstance(fuente, TurbinaEolica): tipo_nombre = "Eólica"
            elif isinstance(fuente, GeneradorDiesel): tipo_nombre = "Diesel"
            
            # Usamos el método polimórfico en lugar de hasattr
            info_extra = fuente.obtener_dato_recurso()
            
            print(f"║ {fuente.id_generador:<10} | {tipo_nombre:<12} | {info_extra:<15} | {fuente.produccion_actual:>11.1f} MW ║")
        print("╚" + "═"*62 + "╝\n")

    def solicitar_entrada(self, mensaje_usuario):
        return input(mensaje_usuario)

    def mostrar_mensaje_sistema(self, texto_mensaje):
        print(f">>> {texto_mensaje}")

# ==========================================
# 4. EL CONTROLADOR (controlador)
# ==========================================
class ControladorRed:
    def __init__(self):
        self.vista_sistema = InterfazRed()
        self.lista_fuentes_energia = []

    def inicializar_sistema(self):
        contenido_json = """
        [
            {"tipo": "solar", "id_generador": "SOL-01", "capacidad_maxima": 100.0},
            {"tipo": "eolica", "id_generador": "EOL-99", "capacidad_maxima": 250.0},
            {"tipo": "diesel", "id_generador": "DSL-05", "capacidad_maxima": 500.0, "combustible": 1000.0}
        ]
        """
        try:
            configuracion_leida = json.loads(contenido_json)
            for datos_unidad in configuracion_leida:
                nueva_unidad = FabricaEnergia.crear_fuente(datos_unidad)
                self.lista_fuentes_energia.append(nueva_unidad)
        except Exception as error_deteccion:
            self.vista_sistema.mostrar_mensaje_sistema(f"Error: {error_deteccion}")

    def ejecutar_simulacion(self):
        self.inicializar_sistema()
        self.vista_sistema.mostrar_tablero(self.lista_fuentes_energia)

        clima_ingresado = self.vista_sistema.solicitar_entrada("Ingrese clima (Soleado/Nublado): ")
        viento_ingresado = self.vista_sistema.solicitar_entrada("Ingrese velocidad del viento: ")
        diesel_ingresado = self.vista_sistema.solicitar_entrada("Litros de diesel para respaldo: ")

        for fuente in self.lista_fuentes_energia:
            if isinstance(fuente, PanelSolar):
                fuente.generar(clima_ingresado)
            elif isinstance(fuente, TurbinaEolica):
                fuente.generar(viento_ingresado)
            elif isinstance(fuente, GeneradorDiesel):
                fuente.generar(diesel_ingresado)

        self.vista_sistema.mostrar_mensaje_sistema("Simulación completada. Actualizando tablero...")
        self.vista_sistema.mostrar_tablero(self.lista_fuentes_energia)

# ==========================================
# PUNTO DE ENTRADA
# ==========================================
if __name__ == "__main__":
    aplicacion_red = ControladorRed()
    aplicacion_red.ejecutar_simulacion()
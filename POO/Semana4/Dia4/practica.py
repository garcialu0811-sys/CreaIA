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

class PanelSolar(FuenteEnergia):
    def generar(self, clima):
        if str(clima).lower() == "soleado":
            self.produccion_actual = self.capacidad_maxima
        else:
            self.produccion_actual = 0.0
        return self.produccion_actual

class TurbinaEolica(FuenteEnergia):
    def generar(self, velocidad_viento):
        # Generación basada en eficiencia (ej. óptimo a 15 km/h o más)
        eficiencia = min(float(velocidad_viento) / 15.0, 1.0)
        self.produccion_actual = self.capacidad_maxima * eficiencia
        return self.produccion_actual

class GeneradorDiesel(FuenteEnergia):
    def __init__(self, id_generador, capacidad_maxima, combustible):
        super().__init__(id_generador, capacidad_maxima)
        self.combustible = float(combustible)

    def generar(self, litros_a_usar):
        litros = float(litros_a_usar)
        if self.combustible >= litros:
            self.combustible -= litros
            self.produccion_actual = self.capacidad_maxima
        else:
            self.produccion_actual = 0.0
        return self.produccion_actual

# ==========================================
# 2. LA FABRICA (fabrica)
# ==========================================
class FabricaEnergia:
    _mapeo = {
        "solar": PanelSolar,
        "eolica": TurbinaEolica,
        "diesel": GeneradorDiesel
    }

    @staticmethod
    def crear_fuente(datos):
        tipo = datos.get("tipo")
        clase = FabricaEnergia._mapeo.get(tipo)
        if not clase:
            raise ValueError(f"Tipo de energía '{tipo}' no reconocido.")
        
        # Filtramos los datos para pasar solo lo que el constructor necesita
        params = {k: v for k, v in datos.items() if k != "tipo"}
        return clase(**params)

# ==========================================
# 3. LA VISTA (vista)
# ==========================================
class InterfazRed:
    def mostrar_tablero(self, fuentes):
        print("\n" + "╔" + "═"*58 + "╗")
        print(f"║ {'ESTADO DE LA RED ELÉCTRICA SMART-CITY':^56} ║")
        print("╠" + "═"*58 + "╣")
        print(f"║ {'ID':<10} | {'TIPO':<15} | {'ESTADO/COMB.':<15} | {'PROD.':<8} ║")
        print("╟" + "─"*58 + "╢")
        for f in fuentes:
            extra = f"{f.combustible:.1f}L" if hasattr(f, 'combustible') else "N/A"
            print(f"║ {f.id_generador:<10} | {type(f).__name__:<15} | {extra:<15} | {f.produccion_actual:>5.1f} MW ║")
        print("╚" + "═"*58 + "╝\n")

    def solicitar_entrada(self, mensaje):
        return input(mensaje)

    def mostrar_mensaje(self, mensaje):
        print(f">>> {mensaje}")

# ==========================================
# 4. EL CONTROLADOR (controlador)
# ==========================================
class ControladorRed:
    def __init__(self):
        self.vista = InterfazRed()
        self.fuentes = []

    def inicializar_sistema(self):
        # Datos proporcionados por el ingeniero
        contenido_json = """
        [
            {"tipo": "solar", "id_generador": "SOL-01", "capacidad_maxima": 100.0},
            {"tipo": "eolica", "id_generador": "EOL-99", "capacidad_maxima": 250.0},
            {"tipo": "diesel", "id_generador": "DSL-05", "capacidad_maxima": 500.0, "combustible": 1000.0}
        ]
        """
        try:
            config = json.loads(contenido_json)
            for item in config:
                nueva_fuente = FabricaEnergia.crear_fuente(item)
                self.fuentes.append(nueva_fuente)
        except Exception as e:
            self.vista.mostrar_mensaje(f"Error cargando config: {e}")

    def ejecutar(self):
        self.inicializar_sistema()
        self.vista.mostrar_tablero(self.fuentes)

        # Captura de datos (Entradas solicitadas)
        clima = self.vista.solicitar_entrada("Ingrese clima (Soleado/Nublado): ")
        viento = self.vista.solicitar_entrada("Ingrese velocidad del viento: ")
        diesel_uso = self.vista.solicitar_entrada("Ingrese litros de diesel para activar respaldo: ")

        # Procesamiento lógico
        for f in self.fuentes:
            if isinstance(f, PanelSolar):
                f.generar(clima)
            elif isinstance(f, TurbinaEolica):
                f.generar(viento)
            elif isinstance(f, GeneradorDiesel):
                f.generar(diesel_uso)

        # Resultado final
        self.vista.mostrar_mensaje("Simulación completada. Actualizando tablero...")
        self.vista.mostrar_tablero(self.fuentes)

# ==========================================
# PUNTO DE ENTRADA
# ==========================================
if __name__ == "__main__":
    app = ControladorRed()
    app.ejecutar()
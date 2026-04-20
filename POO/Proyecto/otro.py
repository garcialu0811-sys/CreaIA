from abc import ABC, abstractmethod  # Importa herramientas para clases abstractas
import random  # Importa random para generar probabilidades aleatorias

class Pokemon(ABC):  # Clase padre abstracta llamada Pokemon
    """
    Clase base abstracta que define la estructura de un Pokémon.
    Implementa encapsulamiento para HP y Energía.
    """
    
    def __init__(self, nombre: str, hp_maximo: int, energia_maxima: int):  # Constructor
        self.nombre = nombre  # Nombre público del Pokémon
        self.hp_maximo = hp_maximo  # Vida máxima pública
        self._hp_actual = hp_maximo  # Vida actual privada
        self.energia_maxima = energia_maxima  # Energía máxima pública
        self._energia_actual = energia_maxima  # Energía actual privada
        self.defendiendo = False  # Estado de defensa público
    
    # ========== Propiedades y Setters (Encapsulamiento) ==========
    
    @property
    def hp_actual(self):  # Getter de hp actual
        return self._hp_actual
    
    @hp_actual.setter
    def hp_actual(self, valor):  # Setter de hp actual
        """Setter que nunca permite valores negativos de HP."""
        if valor < 0:  # Si es menor a 0
            self._hp_actual = 0  # Lo deja en 0
        else:
            self._hp_actual = valor  # Si no, guarda valor normal
    
    @property
    def energia_actual(self):  # Getter de energía actual
        return self._energia_actual
    
    @energia_actual.setter
    def energia_actual(self, valor):  # Setter de energía actual
        """Setter que no permite energía negativa ni mayor al máximo."""
        if valor < 0:  # Si es negativa
            self._energia_actual = 0  # La deja en 0
        elif valor > self.energia_maxima:  # Si supera máximo
            self._energia_actual = self.energia_maxima  # La iguala al máximo
        else:
            self._energia_actual = valor  # Guarda valor normal
    
    # ========== Métodos de Acción ==========
    
    @abstractmethod
    def atacar(self, oponente):  # Método abstracto
        """Método abstracto que será sobrescrito por cada clase hija."""
        pass
    
    def defender(self):  # Método defender
        """
        Acción de defensa: consume 5 EP y reduce el daño del próximo ataque a la mitad.
        """
        costo_ep = 5  # Energía necesaria para defender
        
        if self.energia_actual >= costo_ep:  # Si tiene energía suficiente
            self.energia_actual -= costo_ep  # Resta energía
            self.defendiendo = True  # Activa defensa
            return f"{self.nombre} se ha puesto en guardia. Reducirá el daño del próximo ataque a la mitad."
        else:
            return f"{self.nombre} no tiene suficiente energía para defenderse (Necesita {costo_ep} EP)."
    
    def descansar(self):  # Método descansar
        """
        Acción de descanso: restaura 20 EP pero no ataca.
        """
        restauracion = 20  # Cantidad a recuperar
        self.energia_actual += restauracion  # Suma energía
        self.defendiendo = False  # Quita defensa
        return f"{self.nombre} descansa y recupera {restauracion} EP. Ahora tiene {self.energia_actual}/{self.energia_maxima} EP."
    
    def recibir_dano(self, dano: int):  # Método recibir daño
        """
        Aplica daño al Pokémon.
        """
        dano_final = dano  # Guarda daño inicial
        
        if self.defendiendo:  # Si estaba defendiendo
            dano_final = dano // 2  # Reduce daño a la mitad
            self.defendiendo = False  # Desactiva defensa
        
        self.hp_actual -= dano_final  # Resta vida
        return dano_final  # Retorna daño aplicado
    
    def esta_vivo(self) -> bool:  # Verifica si sigue vivo
        return self.hp_actual > 0
    
    def __str__(self):  # Muestra información del objeto
        return f"{self.nombre} [{self.tipo}] | HP: {self.hp_actual}/{self.hp_maximo} | EP: {self.energia_actual}/{self.energia_maxima}"
    
    @property
    def tipo(self):  # Tipo genérico
        return "Desconocido"


# ========== Clases Hijas ==========

class PokemonAgua(Pokemon):  # Hereda de Pokemon
    
    @property
    def tipo(self):
        return "Agua"
    
    def atacar(self, oponente):
        costo_ep = 15  # Energía necesaria
        
        if self.energia_actual < costo_ep:  # Si no tiene energía
            return f"{self.nombre} no tiene suficiente energía para atacar.", 0
        
        self.energia_actual -= costo_ep  # Resta energía
        dano_base = 20  # Daño base
        
        multiplicador = 1  # Multiplicador normal
        mensaje_efectividad = ""  # Texto vacío
        
        if oponente.tipo == "Fuego":  # Ventaja
            multiplicador = 2
            mensaje_efectividad = "¡Es súper efectivo!"
        elif oponente.tipo == "Planta":  # Desventaja
            multiplicador = 0.5
            mensaje_efectividad = "No es muy efectivo..."
        
        dano_total = int(dano_base * multiplicador)  # Calcula daño total
        dano_real = oponente.recibir_dano(dano_total)  # Aplica daño
        
        mensaje = f"{self.nombre} usa un ataque de AGUA! {mensaje_efectividad} {oponente.nombre} recibe {dano_real} puntos de daño."
        return mensaje, dano_real


class PokemonFuego(Pokemon):
    
    @property
    def tipo(self):
        return "Fuego"
    
    def atacar(self, oponente):
        costo_ep = 15
        
        if self.energia_actual < costo_ep:
            return f"{self.nombre} no tiene suficiente energía para atacar.", 0
        
        self.energia_actual -= costo_ep
        dano_base = 20
        
        multiplicador = 1
        mensaje_efectividad = ""
        
        if oponente.tipo == "Planta":
            multiplicador = 2
            mensaje_efectividad = "¡Es súper efectivo!"
        elif oponente.tipo == "Agua":
            multiplicador = 0.5
            mensaje_efectividad = "No es muy efectivo..."
        
        dano_total = int(dano_base * multiplicador)
        dano_real = oponente.recibir_dano(dano_total)
        
        mensaje = f"{self.nombre} usa un ataque de FUEGO! {mensaje_efectividad} {oponente.nombre} recibe {dano_real} puntos de daño."
        return mensaje, dano_real


class PokemonPlanta(Pokemon):
    
    @property
    def tipo(self):
        return "Planta"
    
    def atacar(self, oponente):
        costo_ep = 15
        
        if self.energia_actual < costo_ep:
            return f"{self.nombre} no tiene suficiente energía para atacar.", 0
        
        self.energia_actual -= costo_ep
        dano_base = 20
        
        multiplicador = 1
        mensaje_efectividad = ""
        
        if oponente.tipo == "Agua":
            multiplicador = 2
            mensaje_efectividad = "¡Es súper efectivo!"
        elif oponente.tipo == "Fuego":
            multiplicador = 0.5
            mensaje_efectividad = "No es muy efectivo..."
        
        dano_total = int(dano_base * multiplicador)
        dano_real = oponente.recibir_dano(dano_total)
        
        mensaje = f"{self.nombre} usa un ataque de PLANTA! {mensaje_efectividad} {oponente.nombre} recibe {dano_real} puntos de daño."
        return mensaje, dano_real


class PokemonElectrico(Pokemon):
    
    @property
    def tipo(self):
        return "Electrico"
    
    def atacar(self, oponente):
        costo_ep = 15
        
        if self.energia_actual < costo_ep:
            return f"{self.nombre} no tiene suficiente energía para atacar.", 0
        
        self.energia_actual -= costo_ep
        dano_base = 20
        
        multiplicador = 1
        mensaje_efectividad = ""
        
        if random.random() < 0.2:  # 20% probabilidad
            oponente.paralizado = True
            mensaje_efectividad = "¡El oponente ha sido paralizado!"
        
        dano_total = int(dano_base * multiplicador)
        dano_real = oponente.recibir_dano(dano_total)
        
        mensaje = f"{self.nombre} usa un ataque ELÉCTRICO! {mensaje_efectividad} {oponente.nombre} recibe {dano_real} puntos de daño."
        return mensaje, dano_real
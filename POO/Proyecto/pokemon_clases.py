from abc import ABC, abstractmethod
import random

class Pokemon(ABC):
    """
    Clase base abstracta que define la estructura de un Pokémon.
    Implementa encapsulamiento para HP y Energía.
    """
    
    def __init__(self, nombre: str, hp_maximo: int, energia_maxima: int):
        self._nombre = nombre
        self._hp_maximo = hp_maximo
        self._hp_actual = hp_maximo
        self._energia_maxima = energia_maxima
        self._energia_actual = energia_maxima
        self._defendiendo = False  # Estado de defensa activa
    
    # ========== Propiedades y Setters (Encapsulamiento) ==========
    
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def hp_actual(self):
        return self._hp_actual
    
    @hp_actual.setter
    def hp_actual(self, valor):
        """Setter que nunca permite valores negativos de HP."""
        if valor < 0:
            self._hp_actual = 0
        else:
            self._hp_actual = valor
    
    @property
    def hp_maximo(self):
        return self._hp_maximo
    
    @property
    def energia_actual(self):
        return self._energia_actual
    
    @energia_actual.setter
    def energia_actual(self, valor):
        """Setter que no permite energía negativa ni mayor al máximo."""
        if valor < 0:
            self._energia_actual = 0
        elif valor > self._energia_maxima:
            self._energia_actual = self._energia_maxima
        else:
            self._energia_actual = valor
    
    @property
    def energia_maxima(self):
        return self._energia_maxima
    
    @property
    def defendiendo(self):
        return self._defendiendo
    
    @defendiendo.setter
    def defendiendo(self, valor):
        self._defendiendo = valor
    
    # ========== Métodos de Acción ==========
    
    @abstractmethod
    def atacar(self, oponente):
        """Método abstracto que será sobrescrito por cada clase hija (Polimorfismo)."""
        pass
    
    def defender(self):
        """
        Acción de defensa: consume 5 EP y reduce el daño del próximo ataque a la mitad.
        """
        costo_ep = 5
        if self.energia_actual >= costo_ep:
            self.energia_actual -= costo_ep
            self.defendiendo = True
            return f"{self.nombre} se ha puesto en guardia. Reducirá el daño del próximo ataque a la mitad."
        else:
            return f"{self.nombre} no tiene suficiente energía para defenderse (Necesita {costo_ep} EP)."
    
    def descansar(self):
        """
        Acción de descanso: restaura 20 EP pero no ataca.
        """
        restauracion = 20
        self.energia_actual += restauracion
        # Cancelamos estado de defensa al descansar
        self.defendiendo = False
        return f"{self.nombre} descansa y recupera {restauracion} EP. Ahora tiene {self.energia_actual}/{self.energia_maxima} EP."
    
    def recibir_dano(self, dano: int):
        """
        Aplica daño al Pokémon, respetando el estado de defensa (reduce a la mitad si está defendiendo).
        """
        dano_final = dano
        if self.defendiendo:
            dano_final = dano // 2
            self.defendiendo = False  # La defensa solo dura un turno
        
        self.hp_actual -= dano_final
        return dano_final
    
    def esta_vivo(self) -> bool:
        """Verifica si el Pokémon aún tiene HP."""
        return self.hp_actual > 0
    
    def __str__(self):
        return f"{self.nombre} [{self.tipo}] | HP: {self.hp_actual}/{self.hp_maximo} | EP: {self.energia_actual}/{self.energia_maxima}"
    
    @property
    def tipo(self):
        """Propiedad que debe ser sobrescrita en las clases hijas."""
        return "Desconocido"


# ========== Clases Hijas (Herencia y Polimorfismo) ==========

class PokemonAgua(Pokemon):
    """Pokémon de tipo Agua - Ventaja contra Fuego (x2)"""
    
    @property
    def tipo(self):
        return "Agua"
    
    def atacar(self, oponente):
        """
        Ataque de Agua.
        - Daño base: 20
        - Costo EP: 15
        - Súper efectivo (x2) contra Fuego
        """
        costo_ep = 15
        
        # Validar energía suficiente
        if self.energia_actual < costo_ep:
            return f"{self.nombre} no tiene suficiente energía para atacar (Necesita {costo_ep} EP).", 0
        
        # Consumir energía
        self.energia_actual -= costo_ep
        dano_base = 20
        
        # Calcular multiplicador según tipo del oponente (Polimorfismo)
        multiplicador = 1
        mensaje_efectividad = ""
        
        if oponente.tipo == "Fuego":
            multiplicador = 2
            mensaje_efectividad = "¡Es súper efectivo!"
        elif oponente.tipo == "Planta":
            multiplicador = 0.5
            mensaje_efectividad = "No es muy efectivo..."
        
        dano_total = int(dano_base * multiplicador)
        
        # Aplicar daño al oponente
        dano_real = oponente.recibir_dano(dano_total)
        
        mensaje = f"{self.nombre} usa un ataque de AGUA! {mensaje_efectividad} {oponente.nombre} recibe {dano_real} puntos de daño."
        return mensaje, dano_real


class PokemonFuego(Pokemon):
    """Pokémon de tipo Fuego - Ventaja contra Planta (x2)"""
    
    @property
    def tipo(self):
        return "Fuego"
    
    def atacar(self, oponente):
        costo_ep = 15
        
        if self.energia_actual < costo_ep:
            return f"{self.nombre} no tiene suficiente energía para atacar (Necesita {costo_ep} EP).", 0
        
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
    """Pokémon de tipo Planta - Ventaja contra Agua (x2)"""
    
    @property
    def tipo(self):
        return "Planta"
    
    def atacar(self, oponente):
        costo_ep = 15
        
        if self.energia_actual < costo_ep:
            return f"{self.nombre} no tiene suficiente energía para atacar (Necesita {costo_ep} EP).", 0
        
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
    """
    Pokémon de tipo Eléctrico - Sin ventaja de daño doble,
    pero con 20% de probabilidad de paralizar al oponente.
    """
    
    @property
    def tipo(self):
        return "Electrico"
    
    def atacar(self, oponente):
        costo_ep = 15
        
        if self.energia_actual < costo_ep:
            return f"{self.nombre} no tiene suficiente energía para atacar (Necesita {costo_ep} EP).", 0
        
        self.energia_actual -= costo_ep
        dano_base = 20
        
        # Eléctrico no tiene ventaja de daño doble, pero puede paralizar
        multiplicador = 1
        mensaje_efectividad = ""
        
        # 20% de probabilidad de paralizar
        if random.random() < 0.2:
            # La paralización se implementará como pérdida del siguiente turno
            # Usamos un atributo temporal en el oponente
            oponente.paralizado = True
            mensaje_efectividad = "¡El oponente ha sido paralizado! Perderá su próximo turno."
        
        dano_total = int(dano_base * multiplicador)
        dano_real = oponente.recibir_dano(dano_total)
        
        mensaje = f"{self.nombre} usa un ataque ELÉCTRICO! {mensaje_efectividad} {oponente.nombre} recibe {dano_real} puntos de daño."
        return mensaje, dano_real
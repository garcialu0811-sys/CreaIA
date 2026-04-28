from abc import ABC, abstractmethod

class NucleoEnergia:
    def __init__(self):
        self.estado = "Operacional"

    # Funcion que ayuda a calcular el nivel de energia despues de una mision
    def consumir(self, cantidad_a_gastar, nivel_actual):
        nuevo_nivel = nivel_actual - cantidad_a_gastar
        # Validacion
        if nuevo_nivel < 0:
            return 0
        else:
            return nuevo_nivel

class NaveEspacial(ABC):
    # Un atributo de clas que es el contador global
    contador_naves = 0

    def  __init__(self, nombre, codigo_registro, nivel_energia):
        self.nombre = nombre
        self.registro = codigo_registro
        self.__energia = nivel_energia
        self.__escudos = 100
        self.estado = "Activo"

        self.nucleo = NucleoEnergia()
        NaveEspacial.incrementar_contador()

    # Metodo de clase para poder llevar el conteo de las naves
    @classmethod
    def incrementar_contador(cls):
        cls.contador_naves += 1
        
    # Decoradores
    @property
    def energia(self):
        return self.__energia
        
    @energia.setter
    def energia(self, valor):
        # Validacion para que la energia este en el rango de 0 a 100
        if valor >= 0 and valor <=100:
            self.__energia = valor
        else:
            print("Error: el nivel de energia debe estar entre 0 y 100")
        
    @property
    def escudos(self):
        return self.__escudos

    @escudos.setter
    def escudos(self, valor):
        # Validacion para ver si el escudo llega a 0, la nave ya sera vulnerable
        if valor < 0:
            self.__escudos = 0
        elif valor > 100:
            self.__escudos = 100
        else:
            self.__escudos = valor
            
        # Si los escudos llegan a fallar que cambie el estado
        if self.__escudos == 0:
            self.estado = "Vulnerable"
    
    # Creacion del metodo abstracto que sobrescribiran las clases hijas
    @abstractmethod
    def mision_especializada(self):
        pass
    
    def __str__(self):
        return f"[{self.registro}] {self.nombre} - Energia: {self.__energia}% - Estado: {self.estado}"

    # Sobrecarga de operador < para poder comparar las naves por su energia
    def __lt__(self, otra_nave_nave):
        return self.__energia < otra_nave_nave.energia

class NaveCombate(NaveEspacial):
    def __init__(self, nombre, codigo_registro, nivel_energia, potencia_fuego):
        super().__init__(nombre, codigo_registro, nivel_energia)
        self.potencia_fuego = potencia_fuego

    def mision_especializada(self):
        return f"Atacando con potencia de {self.potencia_fuego}"

class NaveCarga(NaveEspacial):
    def __init__(self, nombre, codigo_registro, nivel_energia, capacidad):
        super().__init__(nombre, codigo_registro, nivel_energia)
        self.capacidad = capacidad

    def mision_especializada(self):
        return f"Transportando {self.capacidad} toneladas métricas"

    # Sobrecarga de operador + que nos permite fusionar dos naves de carga
    def __add__(self, otra_nave):
        if isinstance(otra_nave, NaveCarga):
            nueva_capacidad = self.capacidad + otra_nave.capacidad
            # Retorna lo que es una nueva nave con las suma de capacidades
            return NaveCarga(f"Fusión-{self.nombre}", "FUSION-99", 100, nueva_capacidad)
        raise ValueError("Solo se pueden fusionar naves de carga.")

# Aplicacimos herencia múltiple
class InterceptorHibrido(NaveCombate, NaveCarga):
    def __init__(self, nombre, codigo_registro, nivel_energia, potencia, capacidad):
        NaveEspacial.__init__(self, nombre, codigo_registro, nivel_energia)
        self.potencia_fuego = potencia
        self.capacidad = capacidad

    def mision_especializada(self):
        return f"Misión Versátil: Combate ({self. potencia_fuego}) y Carga ({self.capacidad})"

class EstacionEspacial:
    def __init__(self):
        self.nombre_estacion = "Aethelgard"
        self.lista_naves_activas = []

    def inyectar_nave(self, objeto_nave):
        self.lista_naves_activas.append(objeto_nave)
    
def ejecutar_estacion():
    centro_mando = EstacionEspacial()

    while True:
        print(f"---- ESTACIÓN AETHELGARD ACTIVADA ----")
        print("1. Registrar Nave")
        print("2. Ejecutar Misión")
        print("3. Comparar Energías")
        print("4. Fusionar")
        print("5. Mostrar Flota")
        print("5. Salir")

        try:
            opcion = input("\nSeleccione una opción: ")

            match opcion:
                case "1":
                    print("Tipo (1. Combate | 2. Carga) | 3. Híbrida")
                    tipo_clase = input("Seleccione tipo: ")
                    nombre = input("Nombre: ")
                    codigo = input("Código: ")

                    if tipo_clase == "1":
                        potencia = int(input("Potencia: "))
                        nueva = NaveCombate(nombre, codigo, 100, potencia)
                    elif tipo_clase == "2":
                        capacidad = int(input("Capacidad: "))
                        nueva = NaveCarga(nombre, codigo, 100, capacidad)
                    elif tipo_clase == "3":
                        potencia = int(input("Potencia: "))
                        capacidad = int(input("Capacidad: "))
                        nueva = InterceptorHibrido(nombre, codigo, 100, potencia, capacidad)
                    else:
                        print("Tipo no reconocido")
                        continue
                    
                    centro_mando.inyectar_nave(nueva)
                    print(f"Éxito. Total histótico fabricado: {NaveEspacial.contador_naves}")
                
                case "2":
                    if len(centro_mando.lista_naves_activas) == 0:
                        print("El hangar está vacío")
                        continue
                    
                    indice = int(input("Índice de la nave a operar (0, 1, 2...): "))
                    energia_mision = int(input("Energía requerida para la misión: "))

                    nave_seleccionada = centro_mando.lista_naves_activas[indice]

                    if energia_mision < 0:
                        print("ERROR: No se puede consumir energia negativa.")
                    elif nave_seleccionada.energia < energia_mision:
                        print("Operacion cancelada: Energia insuficiente")
                    else:
                        nuevo_nivel = nave_seleccionada.nucleo.consumir(energia_mision, nave_seleccionada.energia)
                        nave_seleccionada.energia = nuevo_nivel

                        print(f"Resultado: {nave_seleccionada.ejecutar_estacion()}")
                
                case "3":
                    if len(centro_mando.lista_naves_activas) < 2:
                        print("Faltan naves para comparar.")
                        continue

                    numero1 = centro_mando.lista_naves_activas[0]
                    nuemro2 = centro_mando.lista_naves_activas[1]

                    if numero1 < nuemro2:
                        print(f"{numero1.nombre} tiene menos energia que {nuemro2.nombre}")
                    else:
                        print(f"{numero1.nombre} tiene ifual o mas energia.")

                case "4":
                    print("Seleccione dos naves de carga para fusionar: ")
                    indice1 = int(input("Indice nave 1: "))
                    indice2 = int(input("Indice nave 2: "))
                    nave1 = centro_mando.lista_naves_activas[indice1]
                    nave2 = centro_mando.lista_naves_activas[indice2]

                    nueva_fusion = nave1 + nave2
                    centro_mando.inyectar_nave(nueva_fusion)
                    print(f"Fusion exitosa: {nueva_fusion.nombre}")

                case "5":
                    print("\n ----- REPORTE DE FLOTA ----- ")
                    pos = 0
                    for nave in centro_mando.lista_naves_activas:
                        print(f"ID {pos}: {nave})
        except:
        
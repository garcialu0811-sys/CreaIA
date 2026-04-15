# Ejercicio rápido
Esta programando el sistema de combate de un juego de stae wars. Necesitas gestionar la energía de los Sables de Luz
 * INSTRUCCIONES
1. Importa la libreria ramndom como rd
2. Crea la clase SableDeLuz con un atributo energia (mpieza en 100)
3. Sobrecarga de metodo (recargar): * Si se llama sin argumentos, recupera 10 de energía
    Si se llama con un número, recupera esa cantidad específica.
4. Sobrecarga de operador (-): al restar un SableDeLuz con otro otro objeto SableDeLuz, se bede reducir su energia -10 a no de ellos
5. Funcion log y úsalo para mostrar el estado final


# Concepto Abstracto
```py
class FiguraGeometrica():
    def calcular_area(self):
        print("No sé cómo calcular el área. No soy una figura")

class Cuadrado(FiguraGeometrica):
    def calcular_area(self):
        print("Area = lado * lado")

figura_fantasma = FIguraGeometrica()
figura_fantasma.calcular_area()
```

## Creando el molde fantasma (el módulo `abc`)
- `abc` = Abstract Base Clasess
- Debemos marcar al meno suno de sus metodos con el decorador `@abstractmethod`
- Un metodo abstracto es un metodo vacio. No tiene codigo por dentro. Usamos la palabra `pass`

```py
# Importacion OBLIGATORIA
from abc import ABC, abstractmethod

class Documento(ABC):
    def __init__(self, titulo):
        self.titulo = titulo
    
    @abstractmethod
    def exportar(self):
        pass

    # OPCIONAL: los padres abstractos pueden tener metodos normales
    def mostrar_titulo(self):
        print(f"Documento: {self.titulo}")

try:
    doc_invalido = Documento("Mi archivo")
except:
    print(f"[BLOQUEO DE SEGURIDAD]")
```
**el Hijo ESTÁ OBLIGADO a sobrescribir TODOS los métodos abstractos del Padre**


```py

```

## Propiedades abstractas
Ponemos `@property`seguido de `@abstracrmethod`
*estas obligado a crear un getter para esta propiedad*

```py
from abc import ABC,  abstractmethod

class VehiculoComercial(ABC):
    @property
    @abstractmethod
    def tarifa_km(self):
        pass

    def calcular_viaje(self, kilometro):
        total = kilometro * self.tarifa_km
        print(f"Costo del viaje {total}")

class Taxi(VehiculoComercial):
    @property
    def tarifa_km(self):
        return 500

mi_taxi = Taxi()
mi_taxi.calcular_viaje(10)
```

# Herencia Multiple


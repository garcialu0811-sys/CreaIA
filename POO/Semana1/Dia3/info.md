# Constructor: es un metodo especial
se ejecuta automaticamante en el instante exaxto en el que crearmos el objeto "producto1 = Producto()"

# Sintaxis
"def __init__(self)"
init es una abreviatura de inicializar
__ que termina se concoce como mmetodos de python

# Ejemplo 
```py
class Libro:
    # Nuestro constructor exige 2 ingredientes externos
    def __init__(self, titulo_ingresado, autor_ingresado):
        # Guardamos los ingredientes (atributos) en el interior del objeto
        self.titulo = titulo_ingresado
        self.autor = autor_ingresado
        
# La fabricación
# Aqui vamos a enviar los ingredientes a nuestra clase para crear un objeto
# Viajan directamente a los parentesis del __init__
libro_nuevo = Libro("El Principito", "Antoine de Saint-Exupéry")
libro_viejo = Libro("Don Quijote", "Miguel Cervantes")

# Comprobacion
print(f"El autor registrado del libro {libro_nuevo.titulo} es {libro_nuevo.autor}")
print(f"El autor registrado del libro {libro_viejo.titulo} es {libro_viejo.autor}")

```

# Ejemplo métodos con parámentros normales
```python
class Alcancia:
    # Al nacer, no pide ingredientes (atributos) nuevos
    def __init__(self):
        self.dinero_guardado = 0
    
    #
    def depositar_dinero(self, cantidad):
        # Sumar el parametro al atributo
        self.dinero_guardado += cantidad

    def mostrar_ahorros(self):
        print(f"El dinero ahorrado es: {self.dinero_guardado}")

# Crear un objeto
mi_chanchito = Alcancia()

# Acciones
mi_chanchito.depositar_dinero(500)
mi_chanchito.depositar_dinero(1200)
mi_chanchito.mostrar_ahorros()


alcancia1 = Alcancia()
alcancia1.depositar_dinero(5000)
alcancia1.mostrar_ahorros()
```

# Parámetros opcionales en el constructor



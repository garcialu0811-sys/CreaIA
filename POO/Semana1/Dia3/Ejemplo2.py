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


# El estilo profesional de python (`@property`)
`cliente.pin = 1234`
property se le llama usar decoradores

# Sitanxis del decorador
* Para el Getter: escribimos `@property` justo encima del método. El método DEBE y TIENE que llamarse exactamente igual que el atributo (sin los guines bajos)

* Para los Setter: Escribimos `nombre_del_metodo.setter` justo encima del método modificador.

## Micro ejemplo
```py
class Temperatura:
    def __init__(self):
        self.__grados = 20
    
    @property
    def grados(self):
        return self.__grados
    
    @grados.setter
    def grados(self, nuevo_grado):
        if nuevo_grado < 0:
            print("Temperatura invalida")
        else:
            self.__grados = nuevo_grado
    
clima = Temperatura()
# Con el metodo tradicional, necesitamos usar el clima.get_grados() para obtener el valor de grados
# clima.__grados No funciona

print(clima.grados)
clima.grados = 50
print(clima.grados)
```

# Atributos y metodos de clase
## Atributo de clase
```py
class Tienda:
    #Atributo de la clase(APLICA A TODOS)
    impuetro_iva = 0.13

    def __init__(self, productos):
        self.producto = productos

print(Tienda.impuetro_iva) # 0.13

```
# Metodo de la clase
`@classmethod` --> `cls`
self --> objeto
cls --> class
Se usa exclusivamente para leer o modificar los Atributs de Clase.


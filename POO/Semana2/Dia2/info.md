# Encapsulamiento

getter y setter
Le pondremos candado a la informacion y craremos "Ventanillas de Atencion" (getters y setters) con guardias de seguridad que validaran quien entra y que datos puede modificar


**Sintaxis:** para convertir un atributo publico en **Privado** (invisible para el mundo exterior), simplemente le colocamos dos guiones bajos (`__`) al inicio de su nombre dentro del constructor

### Ejemplo

empleado1
    __nombre
    __edad
    __salario

```py
class Cuenta:
    def __init__(self, saldo_inicial):
        self.nombre = "Pública"
        self.__saldo = saldo_inicial

mi_cuenta = Cuenta(1000)
print(mi_cuenta.nombre)
print(mi_cuenta.__saldo) # ERROR, python no permite acceder a atributos privados desde fuera de la clase
```

## Laas ventanillas de atencion: Getter y Setter (métodos tradicionales)

Construimos metodos publicos especificos llamados *Getters* (Obtenedores) y *Setter* (Configuradores).

    **Getter:** Es un metodo que solo sirve para retornar (`return`) el valor del atributo privado
    **Setter:** Es un metodo que recibe un parametro, lo somete a una calidacion logica (el guardia de seguridad), y si todo esta correcto, modifica el atributo privado
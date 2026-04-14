# Repaso
- herencia
- polimorfismo
- super
- principios SOLID
- sobreescritura de métodos

# Sobrecarga de Operadores
+
5 + 5, 10 (matematicas)
"hola" + "mundo", "Hola Mundo" (concatenando)

billetera1 + billetera2,

## Para enseñar:
- Para enseñar el `+`, sobreescribimos `__add__(self, otro_objeto)` (sumar)
- Para enseñar el `-`, sobreescribimos `__sub__(self, otro objeto)` (restar)
- Para enseñar el `>`, sobreescribimos `__gt__(self, otro_objeto)` (greater than | mayor que)
- Para enseñar el `<`, sobreescribimos `__lt__(self, otro_objeto)` (less than | menor que)
- Para enseñar el `==`, sobreescribimos `__eq__(self, otro_objeto)` (equal | igual)

```py
class Billetera:
    def __init__(self, propietario, monto):
        self.propietario = propietario
        self.monto = monto

    def __add__(self, otra_billetera):
        suma_total = self.monto + otra_billetera.monto

        nuevo_propietario = f"Fondo en conjunto de {self.propietario} y {otra_billetera.propietario}"
        
        return Billetera(nuevo_propietario, suma_total)
    
    def __gt__(self, otra_billetera):
        return self.monto > otra_billetera.monto
    
billetera1 = Billetera("Luis", 1000)
billetera2 = Billetera("Juan", 2500)

if billetera1 > billetera2:
    print("La billetera1 tiene mas efectivo")
else:
    print("La billetera2 tiene mas efectivo")

billetera_familiar = billetera1 + billetera2

print(f"La billetera creada: {billetera_familiar.propietario}")
print(f"El saldo combinado es: {billetera_familiar.monto}")
```

## Ejercicio
- Una
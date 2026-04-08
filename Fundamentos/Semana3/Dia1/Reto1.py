# ## Retos
# ### Reto 1: El Verificador de Edades
# * **Instrucción:** 
# Crea una función llamada `es_mayor_de_edad` que reciba un parámetro llamado `edad`. 
#     * Dentro de la función, evalúa si la edad es mayor o igual a 18.
#     * Si lo es, la función debe DEVOLVER (`return`) el valor booleano `True`. De lo contrario, devolver `False`.
#     * En el programa principal, pide la edad al usuario, llama a la función, y usa el resultado 
# devuelto en un `if` para imprimir "Puedes comprar alcohol" o "Venta denegada".

def es_mayor_de_edad(edad):
    if edad >= 18:
        return True
    else:
        return False

edad = int(input("Ingrese su edad: "))
mayor_edad = es_mayor_de_edad(edad)

if mayor_edad == True:
    print("Puedes comprar alcohol")
else:
    print("Venta denegada")
    
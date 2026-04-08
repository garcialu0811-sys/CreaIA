# ### Reto 2: Calculadora de Descuentos
# * **Instrucción:** 
# Crea una función llamada `aplicar_descuento` que reciba dos parámetros: `precio` y 
# `porcentaje_descuento`. La función debe calcular cuánto dinero se descuenta, 
# restarlo al precio original y usar `return` para devolver el nuevo precio. 
# Pruébala con un artículo de 5000 colones y un descuento del 20%.

def aplicar_descuento(precio, porcentaje_descuento):
    dinero_descontado = precio * (porcentaje_descuento / 100)
    precio_nuevo = precio - dinero_descontado

    return dinero_descontado, precio_nuevo

precio = int(input("Ingrese el precio del producto:"))
porcentaje_descuento = float(input("Ingrese el porcentaje de descuento: "))
nuevo_precio, porcentaje = aplicar_descuento(precio, porcentaje_descuento)

print(f"El nuevo precio del producto es de: {nuevo_precio}")
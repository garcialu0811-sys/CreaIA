#Simular un sistema de escaneo

print("="*15)
print("Escaner de productos")
print("="*15)

#Ejemplo de un break buscando un producto peligroso
for caja in range (1, 11):
    print(f"Escaneando caja {caja}")

    #Simulamos que la caja 5 es un producto peligroso
    if caja == 5:
        print("ALERTA!!!   Producto peligroso encontrado, deteniendo escaneo")
        break

print("El escane ha detenido su revisión de seguridad")


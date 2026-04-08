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



#======================================================================



#Ejemplo de un continue ignorando errores
#Proceso de pagos

print("\n" + "="*15)
print("Porceso de pagos")
print("="*15)

for cliente in range(1, 8):
    print(f"Procesando pago del cliente {cliente}")

    #Simulamos que el cliente 5 tiene un error en su pago 
    #Fondos insuficientes, tarjeta vencida, etc
    if cliente == 5:
        print("ERROR!!!    pago no procesado, saltando al siguiente cliente")
        continue
    print("Pago procesado exitosamente")
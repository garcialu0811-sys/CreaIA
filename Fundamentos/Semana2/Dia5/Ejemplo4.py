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
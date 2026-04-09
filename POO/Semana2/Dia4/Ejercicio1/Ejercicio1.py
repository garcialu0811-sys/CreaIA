# Utilizando la sintaxis
with open ("registro.txt", "r") as archivo_registro:
    # Cree una variable contador que inicie en 0
    cantidad = 0

    # Utilice un ciclo for para leer cada línea. Imprima la linea limpia (usando "strip()") y sume 1 al contador por cada linea leida.
    for linea in archivo_registro:
        texto_limpio = linea.strip()
        print(f"-> {texto_limpio}")
        cantidad += 1

    print(f"Total de líneas leídas: {cantidad}")
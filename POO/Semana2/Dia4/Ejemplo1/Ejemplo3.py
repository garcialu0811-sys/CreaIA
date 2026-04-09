# Leer nuestro archivo

with open("archivo.txt", "r") as archivo_prueba:
    print("Contenido del archivo")

    for linea in archivo_prueba:
        # strip() elimina los espacios en blanco al inicio y al final de la línea y el salto de línea
        texto_limpio = linea.strip()
        print(f"-> {texto_limpio}")
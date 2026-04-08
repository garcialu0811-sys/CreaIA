# Ambito global
nombre_publico = "Diego"

def informacion_privada(nombre):
    # Ambito local
    nombre_privado = "Juan Jose"
    apellido_priado = "Mayen"

    print(f"Mi nombre completo es: {nombre_privado} {apellido_priado}")

    print(f"(local) Mi nombre público es : {nombre}")

    nombre = "Carlos"

    return nombre

nombre_publico = informacion_privada(nombre_publico)

print(f"(global) Mi nombre publico es: {nombre_publico}")
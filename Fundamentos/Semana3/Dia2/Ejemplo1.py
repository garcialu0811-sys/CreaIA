# Ambito global
nombre_publico = "Diego"

def informacion_privada():
    # Ambito local
    nombre_privado = "Juan Jose"
    apellido_priado = "Mayen"

    print(f"Mi nombre completo es: {nombre_privado} {apellido_priado}")

    print(f"Mi nombre público es : {nombre_publico}")

informacion_privada()
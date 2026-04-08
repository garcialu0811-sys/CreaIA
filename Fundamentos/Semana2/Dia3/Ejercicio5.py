#==========================================
#               Ejercicio 5
# Acceso VIP a concierto con compra bebida
#==========================================

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
tipo_entrada = input("¿Cual es su tipo de entrada (general o vip)? ")
dinero = float(input("¿Cuanto dinero tiene disponible? "))
bebida = float(input("¿Cual es el precio de su bebida especial? "))

if edad >= 18 and tipo_entrada == "vip":
    comprar = input("Desea comprar una bebida especial (si/no): ")

    if comprar == "si":
        if dinero >= bebida:
            print("Compra de bebida aprobada.")
            cambio = dinero - bebida
            print("Cambio: ", cambio)
        else:
            print("No puede comprar su bebida porque no cuenta con suficiente dinero.")
else:
    print("No puede ingresar al área VIP")
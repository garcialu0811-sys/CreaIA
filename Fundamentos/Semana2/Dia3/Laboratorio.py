#=======================================
#             Ejercicio 1
#    Control de entrada a un torneo
#=======================================

nombre = input ("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
inscripcion = input("Tiene inscripción confirmada (si/no): ")

if edad >= 15 and inscripcion == "si":
    print("Participante autorizado para ingresar al torneo.")
else:
    print("Participante no autorizado")



#=======================================
#             Ejercicio 2
# Completar código: bateria de celular
#=======================================

bateria = int(input("Ingrese el porcentaje de batería: "))

if bateria <=20:
    print("Debe cargar el celular")
else:
    print("La batería es suficiente")



#=======================================
#             Ejercicio 3
#       Clasificación de envío
#=======================================

peso = float(input("¿Cual es el peso del paquete? "))

if peso < 1:
    print("Paquete liviano.")
elif peso > 5:
    print("Paquete pesado.")
else:
    print("Paquete estándar.")



#=======================================
#             Ejercicio 4
#    Corregir código: semáforo
#=======================================

color = input("Ingrese el color del semáforo: ")

if color == "verde":
    print("Avanzar")
elif color == "amarillo":
    print("Precaución")
else:
    print("Detenerse")



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



#==========================================
#               Ejercicio 6
#    Sistema de becas estudiantiles por 
#      promedio y condición económica
#==========================================

nombre = input("Nombre del estudiante: ")
promedio_final = float(input("Promedio final: "))
ingreso_familiar = int(input("Ingreso familiar mensual: "))
materias_aprobadas = int(input("Materias aprobadas: "))

if promedio_final < 70:
    print("Estudiante: ", nombre)
    print("No recibe beca")
    print("Monto asignado: 0")
elif promedio_final >= 85:
    if materias_aprobadas >= 5 and ingreso_familiar <= 400000:
        print("Estudiante: ", nombre)
        print("Resultado: Beca completa")
        print("Monto asignado: 100,000")
else:
    if ingreso_familiar <= 400000:
        print("Estudiante: ", nombre)
        print("Resultado: Beca parcial")
        print("Monto asignado: 50,000")



#==========================================
#               Ejercicio 7
# Tarifa del hotel con recargo y descuento
#==========================================

nombre_cliente = input("Nombre del cliente: ")
temporada = input("Temporada (alta, media, baja): ")
cantidad_noches = int(input("Cantidad de noches: "))
precio_base = float(input("Precio base por noche: "))
membresia = input("¿Tiene membresía? (si/no) ")

if temporada == "alta":
    if cantidad_noches >= 3 and membresia == "si":
        print("Cliente: ", nombre_cliente)
        recargo = cantidad_noches * precio_base
        subtotal_recargo = recargo * 0.20
        subtotal = recargo + subtotal_recargo
        print("Subtotal con recargo: ", subtotal)
        descuento = subtotal * 0.15
        print("Descuento aplicado: ", descuento)
        total_final = subtotal - descuento
        print("Total final: ", total_final)
    elif cantidad_noches ==2 and membresia == "si":
        print("Cliente: ", nombre_cliente)
        recargo = cantidad_noches * precio_base
        subtotal_recargo = recargo * 0.20
        subtotal = recargo + subtotal_recargo
        print("Subtotal con recargo: ", subtotal)
        descuento = subtotal * 0.05
        print("Descuento aplicado: ", descuento)
        total_final = subtotal - descuento
        print("Total final: ", total_final)
    else:
        print("Cliente: ", nombre_cliente)
        recargo = cantidad_noches * precio_base
        subtotal_recargo = recargo * 0.20
        subtotal = recargo + subtotal_recargo
        print("Subtotal con recargo: ", subtotal)
        print("No se aplica descuento: ")
        print("Total final: ", subtotal)

elif temporada == "media":
    if cantidad_noches >= 3 and membresia == "si":
        print("Cliente: ", nombre_cliente)
        recargo = cantidad_noches * precio_base
        subtotal_recargo = recargo * 0.10
        subtotal = recargo + subtotal_recargo
        print("Subtotal con recargo: ", subtotal)
        descuento = subtotal * 0.15
        print("Descuento aplicado: ", descuento)
        total_final = subtotal - descuento
        print("Total final: ", total_final)
    elif cantidad_noches ==2 and membresia == "si":
        print("Cliente: ", nombre_cliente)
        recargo = cantidad_noches * precio_base
        subtotal_recargo = recargo * 0.10
        subtotal = recargo + subtotal_recargo
        print("Subtotal con recargo: ", subtotal)
        descuento = subtotal * 0.05
        print("Descuento aplicado: ", descuento)
        total_final = subtotal - descuento
        print("Total final: ", total_final)
    else:
        print("Cliente: ", nombre_cliente)
        recargo = cantidad_noches * precio_base
        subtotal_recargo = recargo * 0.10
        subtotal = recargo + subtotal_recargo
        print("Subtotal con recargo: ", subtotal)
        print("No se aplica descuento: ")
        print("Total final: ", subtotal)

else:
    if cantidad_noches >= 3 and membresia == "si":
        print("Cliente: ", nombre_cliente)
        subtotal = (cantidad_noches * precio_base)
        print("Subtotal: ", subtotal)
        descuento = subtotal * 0.15
        print("Descuento aplicado: ", descuento)
        total_final = subtotal - descuento
        print("Total final: ", total_final)
    elif cantidad_noches ==2 and membresia == "si":
        print("Cliente: ", nombre_cliente)
        subtotal = (cantidad_noches * precio_base)
        print("Subtotal: ", subtotal)
        descuento = subtotal * 0.05
        print("Descuento aplicado: ", descuento)
        total_final = subtotal - descuento
        print("Total final: ", total_final)
    else:
        print("Cliente: ", nombre_cliente)
        subtotal = (cantidad_noches * precio_base)
        print("Subtotal: ", subtotal)
        print("No se aplica descuento: ")
        print("Total final: ", subtotal)



#==========================================
#               Ejercicio 8
#     Menú de academia con permisos
#==========================================

print("=== Academia virtual con permisos ===")
print("1. matricular")
print("2. notas")
print("3. certificado")
print("4. salir")

opcion = input("Seleccione una opcion del 1 al 4: ")
usuario = input("Ingrese su tipo de usuario (admin, profesor, estudiante): ")
promedio = float(input("Ingrese su promedio: "))

match opcion:
    case ("matricular" | "1"):
        if usuario == "admin":
            print("Bienvenido administrador a la seccion de matricular")
        if usuario == "profesor":
            print("Bienvenido profesor a la seccion de matricular")
    
    case ("notas" | "2"):
        if usuario == "estudiante":
            print("Bienvenido estudiante a la seccion de notas")
        if usuario == "profesor":
            print("Bienvenido profesor a la seccion de notas")

    case ("certificado" | "3") if  promedio >= 70 and usuario == "estudiante":
        print("Certificado generado correctamente.")
    
    case ("salir" | "4"):
        print("Saliendo...")
    case _:
        print("Error")



#==========================================
#               Ejercicio 9
# Sistema de tienda gamer con promociones
#            y validacion de stock
#==========================================


nombre_cliente = input("Ingrese su nombre: ")
nombre_producto = input("Ingrese nombre del producto: ")
precio_unitario = int(input("Precio unitario del producto: "))
cantidad_deseada = int(input("Cantidad deseada: "))
cantidad_stock = int(input("Cantidad en stock: "))
membresia = input("Tiene membresia gamer ( si / no): ")

if cantidad_deseada > cantidad_stock:
    print("No se puede hacer la venta")
elif cantidad_deseada <= cantidad_stock:
    print("Venta aprobada")
    subtotal = precio_unitario * cantidad_deseada
    print("Subtotal: ", subtotal)
    if subtotal > 50000 and membresia == "si":
        descuento = subtotal * 0.20
        print("Descuento: ", descuento)
        total = subtotal - descuento
        print("Total final: ", total)
    if subtotal > 30000 and membresia == "no":
        descuento = subtotal * 0.10
        print("Descuento: ", descuento)
        total = subtotal - descuento
        print("Total final: ", total)
    else:
        if subtotal < 30000:
            descuento = subtotal * 0
            print("Descuento: ", descuento)
            total = subtotal - descuento
            print("Total final: ", total)



#==========================================
#                 Ejercicio 10
#       Panel de misiones y calculo de 
#                 recompensa
#==========================================

print("=========== VIDEOJUEGO ==========")
print("1. bosque")
print("2. castillo")
print("3. dragón")
print("4. salir")

nombre_jugador = input("Nombre del jugador: ")
clase_jugador = input("Clase del jugador (guerrero, mago, arguero): ")
opcion_mision = input("Opcion de misión: ")
nivel_jugador = int(input("Nivel del jugador: "))
cantidad_derrotados = int(input("Cantidad de enemigos derrotados: "))

match opcion_mision:
    case ("bosque" | "1"):
        if  nivel_jugador >= 1:
            recompensa = cantidad_derrotados * 10
            print("=== Mision bosque completado ===")
            print("Jugador: ", nombre_jugador)
            print("Clase: ", clase_jugador)
            print("Recompensa: ", recompensa)
    case ("castillo" | "2"):
        if nivel_jugador >= 5:
            recompensa = cantidad_derrotados * 20
            print("=== Mision castillo completado ===")
            print("Recompensa base: ", recompensa)
            if clase_jugador == "guerrero":
                bono = 50
                print("Bono adicional: ", bono)
                total = recompensa + bono
                print("Recompensa total: ", total)
            if clase_jugador == "mago":
                bono = 50
                print("Bono adicional: ", bono)
                total = recompensa + bono
                print("Recompensa total: ", total)
            else:
                print("No cumple con el nivel requerido")

    case ("dragón" | "3"):
        if nivel_jugador >= 10:
            recompensa = cantidad_derrotados * 50
            print("=== Mision dragon completado ===")
            print("Recompensa base: ", recompensa)
            if clase_jugador == "guerrero":
                if cantidad_derrotados >= 3:
                    bono = 100
                    print("Bono adicional: ", bono)
            total = recompensa + bono
            print("Recompensa total: ", total)
            if clase_jugador == "arquero":
                if cantidad_derrotados >= 3:
                    bono = 100
                    print("Bono adicional: ", bono)
            total = recompensa + bono
            print("Recompensa total: ", total)
        else:
            print("No cumple con el nivel requerido")
    case _:
        print("No cumple con ninguno de los requisitos")




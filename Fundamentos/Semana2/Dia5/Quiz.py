# ==========================================   
#       Quiz
# Acceso a laboratorio de impresión 3D
# con compra de minutos extra
# ==========================================

nombre_estudiante = input("Nombre del estudiante: ")
edad = int(input("Edad: "))
autorizacion_profesor = input("¿Tiene autorización del profesor? (si/no): ")
saldo_disponible = float(input("Saldo disponible: "))
costo_minutos = float(input("Costo de cada paquete de minutos: "))
total_paquetes = 0

if edad >= 15 and autorizacion_profesor == "si":
    while saldo_disponible >= costo_minutos:
        min_extra = input("¿Desea comprar otro paquete? (si/no): ")
        if min_extra == "si":
            saldo_disponible = saldo_disponible - costo_minutos
            turno = 1
            total_paquetes = total_paquetes + turno
    print("Acceso aprobado al laboratorio para ", nombre_estudiante)
    print("Compra realizada")
    print("Paquetes comprados: ", total_paquetes)
    print("Saldo restante: ", saldo_disponible)
else:
    print("No cumples con una de las condiciones requeridad para ingresar.")
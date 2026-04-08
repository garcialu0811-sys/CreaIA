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
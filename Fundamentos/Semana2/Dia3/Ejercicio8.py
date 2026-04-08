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
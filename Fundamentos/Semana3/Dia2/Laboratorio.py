# Laboratorio listas: El Gestor de Invitados
# Imagina que estás organizando una fiesta VIP. Necesitas un programa que te ayude
#  a controlar quién está en la lista de invitados.
# Instrucciones del Proyecto
# La Lista Principal: Crea una lista vacía llamada lista_invitados.
# Funciones que debes programar:
#   agregar_invitado(nombre): Debe recibir un nombre y usar el método .append() para guardarlo.
#   mostrar_lista(): Debe usar un ciclo for para imprimir todos los nombres que están en la lista actualmente.
#   buscar_invitado(nombre): Debe verificar si un nombre ya está en la lista.
# Si está, devuelve: "El invitado ya está en la lista".
# Si no está, devuelve: "Nombre disponible".
#   eliminar_invitado(nombre): Debe buscar el nombre y usar .remove() para sacarlo de la lista.
# Menú de Usuario:
# Usa un menú para que el portero del evento pueda:
# 1. Registrar nuevo invitado.
# 2. Ver lista completa.
# 3. Eliminar a alguien (por si se porta mal).
# . Salir.

lista_invitados = []

def agregar_invitado(nombre, lista_invitados):
    lista_invitados.append(nombre)

    nombre == nombre
    return nombre

def mostrar_lista(lista_invitados):
        print(lista_invitados)

def buscar_invitado(nombre, lista_invitados):
    for nombre in lista_invitados:
        if nombre == lista_invitados:
            return True
        else:
            return False

def eliminar_invitado(nombre, lista_invitados):
    if nombre == lista_invitados:
        lista_invitados.remove(nombre)
        print("Invitado eliminado")
    else:
        print("Invitado no existe en la lista")
    
    return lista_invitados

def menu_invitados():
    print("1. Registrar nuevo invitado")
    print("2. Ver lista completa")
    print("3. Eliminar a alguien")
    print("4. Salir")

    opcion = input("Seleccione una opcion: ")
    
    while True:
        match opcion:
            case "1":
                nombre = input("Ingrese el nombre del invitado: ")
                nombre_invitado = agregar_invitado(nombre, lista_invitados)

                invitado_buscado = buscar_invitado(nombre, lista_invitados)

                if invitado_buscado == True:
                    print("El invitado ya está en la lista.")
                else:
                    print("Nombre disponible.")
                    
            case "2":
                mostrar_lista(lista_invitados)
            case "3":
                nombre = input("Ingrese el nombre del invitado que desea eliminar: ")
                eliminar_invitado(nombre, lista_invitados)

            case "4":
                print("Saliendo...")
                break
            case _:
                print("Opcion no valida")

        opcion = input("Seleccione un opcion: ")

menu_invitados()
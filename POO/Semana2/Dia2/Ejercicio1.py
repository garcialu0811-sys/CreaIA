class RegistroAcademico:
    def __init__(self, nombre_alumno, nota_inicial):
        self.nombre = nombre_alumno
        self.__nota = nota_inicial
        self.cuenta_activa = True
    
    def get_nota(self):
        return self.__nota
    
    def bloquear_cuenta(self):
        self.cuenta_activa = False
    
    def set_nota(self, nueva_nota):
        if self.cuenta_activa == False:
            return -2
        elif 0 <= nueva_nota <= 100:
            self.__nota = nueva_nota
            return 1
        else:
            return -1


registro = RegistroAcademico("Laura", 85)

intentos_permitidos = 3
while intentos_permitidos > 0:
    nueva_nota = int(input(f"Ingrese la nueva nota para el alumno/a {registro.nombre}: "))
    resultado = registro.set_nota(nueva_nota)

    if resultado == 1:
        print("¡Felicidades! Nota actualizada correctamente.")
        print(f"La nueva nota de {registro.nombre} es: {registro.get_nota()}")
        break
    elif resultado == -1:
        intentos_permitidos -= 1
        print(f"ERROR, ingrese una nota valida. le queda {intentos_permitidos} intentos.")

if intentos_permitidos == 0:
    registro.bloquear_cuenta()
    print(f"Llego al limite de intentos. La cuenta de {registro.nombre} ha sido bloqueada.")

from abc import ABC, abstractmethod

class PersonalMedico(ABC):
    def __init__(self, nombre_completo, especialidad_medica):
        self.nombre = nombre_completo
        self.especialidad = especialidad_medica

    @abstractmethod
    def realizar_labor(self):
        pass

class Doctor(PersonalMedico):
    def realizar_labor(self):
        print(f"[SISTEMA] El Dr. {self.nombre} está realizando un diagnóstico especializado.")

    def atender_paciente(self, paciente_objetivo):
        self.realizar_labor()
        
        nota_diagnostico = input("Ingrese nota para el historial: ")
        paciente_objetivo.historial.agregar_observacion(nota_diagnostico)
        
        while True:
            try:
                cantidad_medicina = input("Ingrese dosis de recuperación (1-50): ")
                dosis_numerica = int(cantidad_medicina)
                
                paciente_objetivo.salud += dosis_numerica
                if paciente_objetivo.salud > 100: 
                    paciente_objetivo.salud = 100
                
                paciente_objetivo.verificar_estado_salud()
                print(f"¡Tratamiento Exitoso! La salud de {paciente_objetivo.nombre} ha subido a {paciente_objetivo.salud}%.")
                break
            except ValueError:
                print("[ERROR]: Solo se permiten valores numéricos para la dosis. Intente de nuevo.")

class Enfermero(PersonalMedico):
    def realizar_labor(self):
        print(f"[SISTEMA] El Enfermero {self.nombre} está aplicando cuidados y revisando signos vitales.")

class HistorialClinico:
    def __init__(self):
        self.lista_observaciones = []

    def agregar_observacion(self, texto_nota):
        self.lista_observaciones.append(texto_nota)

    def mostrar_notas_registradas(self):
        for indice, nota in enumerate(self.lista_observaciones, 1):
            print(f"  {indice}. {nota}")

class Paciente:
    def __init__(self, nombre_paciente, edad_años, porcentaje_salud=100):
        self.nombre = nombre_paciente
        self.edad = edad_años
        self.salud = porcentaje_salud
        self.estado_clinico = "Estable"
        self.historial = HistorialClinico()
        self.verificar_estado_salud()

    def verificar_estado_salud(self):
        if self.salud < 20:
            self.estado_clinico = "CRÍTICO"
        else:
            self.estado_clinico = "Estable"

class Hospital:
    def __init__(self):
        self.nomina_pacientes = []
        self.nomina_personal = []

    def registrar_nuevo_paciente(self):
        try:
            nombre = input("Nombre del paciente: ")
            edad = int(input("Edad: "))
            salud_inicial = int(input("Salud inicial (0-100): "))
            nuevo_paciente = Paciente(nombre, edad, salud_inicial)
            self.nomina_pacientes.append(nuevo_paciente)
            print("Paciente registrado con éxito.")
        except ValueError:
            print("[ERROR]: Datos numéricos inválidos.")

    def contratar_personal_medico(self):
        nombre = input("Nombre del profesional: ")
        area = input("Especialidad/Área: ")
        tipo_empleado = input("Tipo (1. Doctor / 2. Enfermero): ")
        
        if tipo_empleado == "1":
            nuevo_miembro = Doctor(nombre, area)
        else:
            nuevo_miembro = Enfermero(nombre, area)
            
        self.nomina_personal.append(nuevo_miembro)
        print("Personal contratado.")

    def generar_reporte_pabellon(self):
        print("\n" + "="*50)
        print(f"{'NOMBRE PACIENTE':<20} | {'EDAD':<5} | {'SALUD':<8} | {'ESTADO'}")
        print("-" * 50)
        for p in self.nomina_pacientes:
            print(f"{p.nombre:<20} | {p.edad:<5} | {p.salud:<7}% | {p.estado_clinico}")
        print("="*50 + "\n")

def ejecutar_sistema():
    administracion_hospital = Hospital()
    while True:
        print("\n>>> CONTROL HOSPITALARIO VIDA-SANA <<<")
        print("1. Registrar Paciente\n2. Contratar Personal\n3. Realizar Consulta\n4. Ver Reporte\n5. Salir")
        
        seleccion = input("Seleccione una opción: ")

        if seleccion == "1":
            administracion_hospital.registrar_nuevo_paciente()
        elif seleccion == "2":
            administracion_hospital.contratar_personal_medico()
        elif seleccion == "3":
            if not administracion_hospital.nomina_personal or not administracion_hospital.nomina_pacientes:
                print("[!] Datos insuficientes para consulta.")
                continue
            
            print("\n--- Personal Disponible ---")
            for i, p in enumerate(administracion_hospital.nomina_personal):
                print(f"{i}. {p.nombre} ({p.especialidad})")
            id_medico = int(input("Seleccione médico: "))

            print("\n--- Pacientes en Espera ---")
            for i, p in enumerate(administracion_hospital.nomina_pacientes):
                print(f"{i}. {p.nombre} ({p.salud}% - {p.estado_clinico})")
            id_paciente = int(input("Seleccione paciente: "))

            profesional = administracion_hospital.nomina_personal[id_medico]
            sujeto_atencion = administracion_hospital.nomina_pacientes[id_paciente]

            if isinstance(profesional, Doctor):
                profesional.atender_paciente(sujeto_atencion)
            else:
                profesional.realizar_labor()

        elif seleccion == "4":
            administracion_hospital.generar_reporte_pabellon()
        elif seleccion == "5":
            print("Cerrando sistema...")
            break

if __name__ == "__main__":
    ejecutar_sistema()
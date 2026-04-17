from abc import ABC, abstractmethod

# Uso de Clase Abstracta (PersonalMedico) para definir un molde base.
# Se hereda de ABC para evitar que se puedan instanciar objetos genéricos de esta clase,
# asegurando que todo personal sea obligatoriamente un Doctor o un Enfermero.
class PersonalMedico(ABC):
    def __init__(self, nombre_completo, especialidad_medica):
        self.nombre = nombre_completo
        self.especialidad = especialidad_medica
        self.tipo_profesional = "" 

    # Método abstracto: obliga a todas las subclases a implementar su propia versión
    # de 'realizar_labor', aplicando así el concepto de Polimorfismo.
    @abstractmethod
    def realizar_labor(self):
        pass

# Herencia: Doctor extiende a PersonalMedico, reutilizando su constructor y atributos.
class Doctor(PersonalMedico):
    def __init__(self, nombre_completo, especialidad_medica):
        super().__init__(nombre_completo, especialidad_medica)
        self.tipo_profesional = "doctor"

    # Implementación específica del método abstracto (Polimorfismo).
    def realizar_labor(self):
        print(f"\n[SISTEMA] El Dr. {self.nombre} está realizando un diagnóstico especializado.")

    def atender_paciente(self, paciente_objetivo):
        self.realizar_labor()
        
        # Interacción directa con el objeto paciente y su historial (Composición).
        nota_diagnostico = input("Ingrese nota para el historial: ")
        paciente_objetivo.historial.agregar_observacion(nota_diagnostico)
        
        # Validación de entrada de datos para asegurar la integridad del programa.
        while True:
            try:
                cantidad_medicina = input("Ingrese dosis de recuperación (1-50): ")
                dosis_numerica = int(cantidad_medicina)
                
                paciente_objetivo.salud += dosis_numerica
                if paciente_objetivo.salud > 100: 
                    paciente_objetivo.salud = 100
                
                # Actualización de estado basada en la nueva salud.
                paciente_objetivo.verificar_estado_salud()
                print(f"\n¡Tratamiento Exitoso! La salud de {paciente_objetivo.nombre} ha subido a {paciente_objetivo.salud}%.")
                break
            except ValueError:
                print("[ERROR]: Solo se permiten valores numéricos para la dosis. Intente de nuevo.")

class Enfermero(PersonalMedico):
    def __init__(self, nombre_completo, especialidad_medica):
        super().__init__(nombre_completo, especialidad_medica)
        self.tipo_profesional = "enfermero"

    def realizar_labor(self):
        print(f"\n[SISTEMA] El Enfermero {self.nombre} está aplicando cuidados y revisando signos vitales.")

# Clase HistorialClinico: Ejemplo de modularidad para organizar los datos médicos.
class HistorialClinico:
    def __init__(self):
        self.lista_observaciones = []

    def agregar_observacion(self, texto_nota):
        self.lista_observaciones.append(texto_nota)

    def mostrar_notas_registradas(self):
        numero_nota = 1
        for nota in self.lista_observaciones:
            print(f"  {numero_nota}. {nota}")
            numero_nota += 1

# Clase Paciente: Encapsula los datos del sujeto y gestiona su propio estado clínico.
class Paciente:
    def __init__(self, nombre_paciente, edad_años, porcentaje_salud=100):
        self.nombre = nombre_paciente
        self.edad = edad_años
        self.salud = porcentaje_salud
        self.estado_clinico = "Estable"
        # Relación de Composición: Un Paciente TIENE UN Historial Clínico.
        self.historial = HistorialClinico()
        self.verificar_estado_salud()

    # Lógica interna para determinar la gravedad del paciente automáticamente.
    def verificar_estado_salud(self):
        if self.salud < 20:
            self.estado_clinico = "CRÍTICO"
        else:
            self.estado_clinico = "Estable"

# Clase Controladora (Hospital): Gestiona las colecciones de objetos y el flujo de trabajo.
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
        
        # Instanciación dinámica basada en la elección del usuario.
        if tipo_empleado == "1":
            nuevo_miembro = Doctor(nombre, area)
            self.nomina_personal.append(nuevo_miembro)
            print("Doctor contratado.")
        elif tipo_empleado == "2":
            nuevo_miembro = Enfermero(nombre, area)
            self.nomina_personal.append(nuevo_miembro)
            print("Enfermero contratado.")
        else:
            print("[ERROR]: Opción de tipo de personal no válida.")

    # Generación de reportes formateados para facilitar la lectura de datos.
    def generar_reporte_pabellon(self):
        print("\n" + "="*50)
        print(f"{'NOMBRE PACIENTE':<20} | {'EDAD':<5} | {'SALUD':<8} | {'ESTADO'}")
        print("-" * 50)
        for paciente_actual in self.nomina_pacientes:
            print(f"{paciente_actual.nombre:<20} | {paciente_actual.edad:<5} | {paciente_actual.salud:<7}% | {paciente_actual.estado_clinico}")
        print("="*50 + "\n")

# Función principal 
def ejecutar_sistema():
    administracion_hospital = Hospital()
    
    while True:
        print("\n>>> SISTEMA HOSPITALARIO VIDA-SANA <<<<<<")
        print("1. Registrar Paciente")
        print("2. Contratar Personal")
        print("3. Realizar Consulta Médica")
        print("4. Ver Reporte de Pabellón")
        print("5. Salir")
        
        seleccion = input("\nSeleccione una opción: ")

        match seleccion:
            case "1":
                administracion_hospital.registrar_nuevo_paciente()
            
            case "2":
                administracion_hospital.contratar_personal_medico()
            
            case "3":
                # Validación preventiva para evitar errores al operar con listas vacías.
                if not administracion_hospital.nomina_personal or not administracion_hospital.nomina_pacientes:
                    print("[!] Datos insuficientes para consulta.")
                    continue
                
                # Selección de personal
                print("\n--- Personal Disponible ---")
                for indice_medico in range(len(administracion_hospital.nomina_personal)):
                    personal = administracion_hospital.nomina_personal[indice_medico]
                    print(f"{indice_medico}. {personal.nombre} ({personal.especialidad})")
                
                try:
                    id_seleccionado_medico = int(input("Seleccione médico: "))
                    
                    # Selección de paciente
                    print("\n--- Pacientes en Espera ---")
                    for indice_paciente in range(len(administracion_hospital.nomina_pacientes)):
                        paciente = administracion_hospital.nomina_pacientes[indice_paciente]
                        print(f"{indice_paciente}. {paciente.nombre} ({paciente.salud}% - {paciente.estado_clinico})")
                    
                    id_seleccionado_paciente = int(input("Seleccione paciente: "))

                    profesional = administracion_hospital.nomina_personal[id_seleccionado_medico]
                    sujeto_atencion = administracion_hospital.nomina_pacientes[id_seleccionado_paciente]

                    # Aplicación de Polimorfismo según el tipo de objeto instanciado.
                    if profesional.tipo_profesional == "doctor":
                        profesional.atender_paciente(sujeto_atencion)
                    else:
                        profesional.realizar_labor()
                except (ValueError, IndexError):
                    print("[ERROR]: Selección de ID no válida.")

            case "4":
                administracion_hospital.generar_reporte_pabellon()
            
            case "5":
                print("Cerrando sistema...")
                break

            # capturando cualquier entrada que no coincida con los patrones anteriores.
            case _:
                print("[!] Opción inválida, intente de nuevo.")


ejecutar_sistema()
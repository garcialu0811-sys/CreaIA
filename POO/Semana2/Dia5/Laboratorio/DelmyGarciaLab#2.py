# =================================================================
#        LABORATORIO: SISTEMA DE MONITOREO DE PRESIÓN
# =================================================================

class SensorPresion:
    # Atributos de Clase obligatorios
    LIMITE_PELIGRO = 200 
    total_lecturas = 0 
    
    def __init__(self, nombre_del_sensor):
        # Atributo privado obligatorio __presion [cite: 132, 186]
        self.__presion = 0
        self.nombre = nombre_del_sensor

    @property
    def presion(self):
        return self.__presion
    
    @presion.setter
    def presion(self, valor_nuevo):
        if valor_nuevo < 0:
            self.__presion = 0
        else:
            self.__presion = valor_nuevo

def procesar_monitoreo():
    # Lista para almacenar los objetos procesados 
    lista_sensores = []
    
    print("-" * 40)
    print("  SISTEMA DE MONITOREO INDUSTRIAL")
    print("-" * 40)
    print("Leyendo registros de presión...") 

    # Apertura segura de archivos con 'with open'
    with open("registros.txt", "r") as archivo_lectura:
        # Leemos el archivo línea por línea 
        for linea in archivo_lectura:
            nombre_caldera = linea.strip() 
            
            if nombre_caldera != "":
                # Leemos la siguiente línea inmediatamente para obtener la presión 
                valor_texto = archivo_lectura.readline().strip()
                presion_num = int(valor_texto) # Conversión a entero 
                
                # Instanciamos y usamos el setter [
                nuevo_sensor = SensorPresion(nombre_caldera)
                nuevo_sensor.presion = presion_num
                
                # Guardamos en la lista y aumentamos el contador global
                lista_sensores.append(nuevo_sensor)
                SensorPresion.total_lecturas += 1

    # Procesamiento de alertas y generación de archivo 
    contador_alertas = 0
    with open("alertas.txt", "w") as archivo_alertas:
        archivo_alertas.write("REPORTE DE INCIDENCIAS\n")
        
        for sensor in lista_sensores:
            # Evaluación de riesgo contra el límite global 
            if sensor.presion > SensorPresion.LIMITE_PELIGRO:
                estado = "¡PELIGRO!" 
                contador_alertas += 1
                # Escribimos en el archivo según el formato solicitado
                archivo_alertas.write(f"{contador_alertas}. {sensor.nombre}\n")
            else:
                estado = "Seguro"
            
            # Salida en consola según simulación
            print(f"Analizando: {sensor.nombre} | Estado: {estado}")

        archivo_alertas.write("CALDERAS CRÍTICAS\n") 

    # Resumen final en terminal 
    print("-" * 40)
    print(f"[AUDITORÍA] Se han generado alertas en 'alertas.txt'")
    print(f"[RESUMEN] Total de sensores procesados: {SensorPresion.total_lecturas}.")

# Ejecución del sistema
procesar_monitoreo()
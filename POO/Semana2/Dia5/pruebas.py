
class SensorPresion:
    # Atributos de Clase (Constantes y Contadores)
    LIMITE_PELIGRO = 200
    total_lecturas = 0

    def __init__(self, nombre_del_sensor):
        self.nombre = nombre_del_sensor
        # Atributo privado obligatorio (Encapsulamiento)
        self.__presion = 0

    @property
    def presion(self):
        """Getter para obtener el valor privado."""
        return self.__presion

    @presion.setter
    def presion(self, valor_ingresado):
        """Setter con validación de lógica de negocio."""
        if valor_ingresado < 0:
            print(f"[ADVERTENCIA]: Valor negativo corregido a 0 en {self.nombre}.")
            self.__presion = 0
        else:
            self.__presion = valor_ingresado



def procesar_monitoreo():
    # Contador local para el archivo de alertas
    cantidad_sensores_criticos = 0
    
    print(">>> INICIANDO PROCESAMIENTO DE REGISTROS <<<")

    # Abrimos los archivos usando 'with' para asegurar el cierre automático
    with open("registros.txt", "r") as archivo_entrada:
        with open("alertas.txt", "w") as archivo_salida:
            
            # Escribir encabezado en el archivo
            archivo_salida.write("REPORTE DE INCIDENCIAS\n")
            archivo_salida.write("=" * 30 + "\n")

            for linea in archivo_entrada:
                # Limpiar espacios y saltos de línea
                linea_limpia = linea.strip()
                
                if linea_limpia != "":
                    # Separar nombre de la presión
                    datos = linea_limpia.split(",")
                    nombre_sensor = datos[0]
                    valor_presion = int(datos[1])

                    # Crear objeto y asignar presión (activando validación)
                    sensor_actual = SensorPresion(nombre_sensor)
                    sensor_actual.presion = valor_presion
                    
                    # Incrementar contador global de la clase
                    SensorPresion.total_lecturas += 1

                    # Determinar estado para la simulación en consola
                    if sensor_actual.presion > SensorPresion.LIMITE_PELIGRO:
                        estado_consola = "[PELIGRO]"
                        cantidad_sensores_criticos += 1
                        # Escribir en el archivo de alertas
                        archivo_salida.write(f"{cantidad_sensores_criticos}. {sensor_actual.nombre}\n")
                    else:
                        estado_consola = "[SEGURO]"

                    # Imprimir en consola tal como aparece en la simulación del PDF
                    print(f"Analizando: {sensor_actual.nombre} | Presión: {sensor_actual.presion} | Estado: {estado_consola}")

            # Escribir el resumen final en el archivo de texto
            archivo_salida.write("=" * 30 + "\n")
            archivo_salida.write(f"RESUMEN DEL MONITOREO:\n")
            archivo_salida.write(f"- Total de lecturas: {SensorPresion.total_lecturas}\n")
            archivo_salida.write(f"- Sensores críticos: {cantidad_sensores_criticos}\n")
            archivo_salida.write("\nCALDERAS CRÍTICAS")

    print(">>> PROCESAMIENTO COMPLETADO CON ÉXITO <<<")
    print("Archivo 'alertas.txt' generado correctamente.")

# --- Ejecución del Sistema ---
procesar_monitoreo()

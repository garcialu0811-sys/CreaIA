

class SensorPresion:
    # Atributos de Clase
    LIMITE_PELIGRO = 200
    total_lecturas = 0

    def __init__(self, nombre_del_sensor):
        self.nombre = nombre_del_sensor
        # Atributo privado (Encapsulamiento)
        self.__presion = 0

    @property
    def presion(self):
        return self.__presion

    @presion.setter
    def presion(self, valor_recibido):
        if valor_recibido < 0:
            self.__presion = 0
        else:
            self.__presion = valor_recibido

def procesar_monitoreo():
    cantidad_sensores_criticos = 0
    
    print(">>> INICIANDO PROCESAMIENTO DE REGISTROS <<<")

    with open("registros.txt", "r") as archivo_entrada:
        with open("alertas.txt", "w") as archivo_salida:
            
            archivo_salida.write("REPORTE DE INCIDENCIAS\n")
            archivo_salida.write("=" * 30 + "\n")

            for linea in archivo_entrada:
                linea_limpia = linea.strip()
                
                if linea_limpia != "":
                    # --- SEPARACIÓN CARÁCTER POR CARÁCTER (Sin split ni find) ---
                    indice_coma = 0
                    posicion_actual = 0
                    
                    # Recorremos la línea para encontrar dónde está la coma
                    for caracter in linea_limpia:
                        if caracter == ",":
                            indice_coma = posicion_actual
                        posicion_actual += 1
                    
                    # Usamos rebanado (slicing) con el índice encontrado
                    nombre_sensor = linea_limpia[:indice_coma]
                    valor_texto_presion = linea_limpia[indice_coma + 1:]
                    valor_presion = int(valor_texto_presion)
                    # ------------------------------------------------------------

                    # Crear objeto y procesar
                    sensor_actual = SensorPresion(nombre_sensor)
                    sensor_actual.presion = valor_presion
                    
                    SensorPresion.total_lecturas += 1

                    # Lógica de estado y salida en consola
                    if sensor_actual.presion > SensorPresion.LIMITE_PELIGRO:
                        estado_consola = "[PELIGRO]"
                        cantidad_sensores_criticos += 1
                        archivo_salida.write(f"{cantidad_sensores_criticos}. {sensor_actual.nombre}\n")
                    else:
                        estado_consola = "[SEGURO]"

                    print(f"Analizando: {sensor_actual.nombre} | Presión: {sensor_actual.presion} | Estado: {estado_consola}")

            # Escribir resumen final en el archivo
            archivo_salida.write("=" * 30 + "\n")
            archivo_salida.write(f"RESUMEN DEL MONITOREO:\n")
            archivo_salida.write(f"- Total de lecturas: {SensorPresion.total_lecturas}\n")
            archivo_salida.write(f"- Sensores críticos: {cantidad_sensores_criticos}\n")
            archivo_salida.write("\nCALDERAS CRÍTICAS")

    print(">>> PROCESAMIENTO COMPLETADO CON ÉXITO <<<")
    print("Archivo 'alertas.txt' generado correctamente.")

# --- Ejecución del Programa ---
procesar_monitoreo()
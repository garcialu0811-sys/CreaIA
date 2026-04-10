# Creacion de la clase SensorPresion
class SensorPresion:
    # Creacion de variables de clase
    total_lecturas = 0
    limite_peligroso = 200
    
    # Creacion del constructor de la clase 
    def __init__(self, nombre_del_sensor):
        # Creacion del atributo privado __presion
        self.__presion = 0
        self.nombre = nombre_del_sensor

    # Creacion de @property para el atributo privado __presion que actua como getter
    @property
    def presion(self):
        return self.__presion
    
    # Creacion de su respectivo @presion.setter para el atributo privado __presion que actua como setter
    @presion.setter
    def presion(self, valor_presion):
        if valor_presion < 0:
            print("[ERROR] La presion no puede ser negativa.")
        else:
            self.__presion = valor_presion


def procesar_monitoreo():
    #se crea un contador local para el archivo de alertas
    cantidad_sensores_alerta = 0

    print("=" * 50)
    print(f"{" --- SISTEMA DE MONITOREO INDUSTRIAL --- ":^50}")

    # Creacion de with open para la lectura del archivo registros.txt y la creacion del archivo de alertas.txt
    with open("registros.txt", "r") as archivo_de_lectura:
        with open("alertas.txt", "w") as archivo_de_escritura:

            archivo_de_escritura.write("--- REPORTE DE INCIDENCIAS - CALDERAS CRÍTICAS ---\n")
            archivo_de_escritura.write("=" * 50 + "\n")

            for linea in archivo_de_lectura:
                # Limpiamos espacios y saltos de línea
                linea_limpia = linea.strip()

                if linea_limpia != "":
                    indice_coma = 0
                    posicion_actual = 0

                    nombre_sensor = linea_limpia[:indice_coma]
                    valor_text_presion = linea_limpia[indice_coma + 1:]
                    valor_presion = int(valor_text_presion)

                    # Creamos objeto y procesar
                    sensor_actual = SensorPresion(nombre_sensor)
                    sensor_actual.presion = valor_presion

                    # Incrementamos el contador de lecturas totales
                    SensorPresion.total_lecturas += 1

                    # Determinamos el estado para la simulacion en consola
                    if sensor_actual.presion > SensorPresion.limite_peligroso:
                        estado = "¡PELIGRO!"
                        cantidad_sensores_alerta += 1
                        archivo_de_escritura.write(f"Sensor: {sensor_actual.nombre} - Presión: {sensor_actual.presion} - Estado: {estado}\n")
                    else:
                        estado = "Seguro"
                    
                    print(f"Analizando: {sensor_actual.nombre} | Estado: {estado}")
            
            # Escribimos el resumen final en el archivo de alertas
            archivo_de_escritura.write("\n" + "=" * 50 + "\n")
            archivo_de_escritura.write(f"{"--- RESUMEN FINAL ---":^50}\n")
            archivo_de_escritura.write(f"Total de lecturas: {SensorPresion.total_lecturas}\n")
            archivo_de_escritura.write(f"Sensores en estado crítico: {cantidad_sensores_alerta}\n")
            archivo_de_escritura.write(f"{"--- CALDERAS CRÍTICAS ---":^50}\n")
        
    print(f"{'--- PROCESAMIENTO COMPLETADO CON EXITO ---':^50}")
    print("Archivo \"alertas.txt\" creado exitosamente.")

# Llamamos a la funcion para procesar el monitoreo
procesar_monitoreo()




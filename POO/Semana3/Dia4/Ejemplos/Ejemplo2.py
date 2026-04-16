class Procesador:
    def __init__(self, modelo):
        self.modelo = modelo

class TarjetaVideo:
    def __init__(self, memoria_gb):
        self.memoria = memoria_gb

class Computadora:
    def __init__(self, cpu_externa, gpu_externa):
        self.cpu = cpu_externa
        self.gpu = gpu_externa
    
    def mostrar_especificaciones(self):
        print("\nEspecificaciones del equipo: ")

        # Accedemos a los atributos de las piezas inyectadas
        print(f"- Procesador: {self.cpu.modelo}")
        print(f"- Gráficos: {self.gpu.memoria} GB de video")

# Fabricar las piezas por separado
intel_i9 = Procesador("Intel Core i9 14900K")
nvidia_x = TarjetaVideo(24)

pc_gamer = Computadora(intel_i9, nvidia_x)
pc_gamer.mostrar_especificaciones()
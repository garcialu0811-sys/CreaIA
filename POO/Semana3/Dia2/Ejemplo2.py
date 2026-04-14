print("\n--- SIMULACION DE SOBRECARGA DE METODOS ---")

class CalculadoraRRHH:
    # Un solo metodo maneja 1, 2 o 3 ingredientes sin cola´sar
    def procesar_pago(self, salario_base, bono=0, deducciones=0):
        print(f"\nProcesando pago (Base: {salario_base}, Bono: {bono}, Deducciones: {deducciones})")

        # La navaja suiza analiza el contexto
        total = salario_base + bono - deducciones
        print(f"Total a deposital: ${total}")

# --- USO ---
sistema = CalculadoraRRHH()

# El mismo metódo exacto soporta 3 formas distintas de uso:
sistema.procesar_pago(500000) # Solo recibe 1 parametro
sistema.procesar_pago(500000, 50000) # Recibe 2 parametros
sistema.procesar_pago(500000, 50000, 10000) # Recibe 3 parametros
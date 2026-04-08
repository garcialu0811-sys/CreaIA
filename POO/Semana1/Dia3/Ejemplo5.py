class Televisor:

    def __init__(self, marca):
        self.marca = marca
        self.encendido = False      # Estado inicial en apagado
        self.volumen = 10           # Estado inicial: volumen 10

    def presionar_boton_encendido(self):
        # Si esta apagado (false), lo prendemos (true)
        if self.encendido == False:
            self.encendido = True
            print(f"El televisor {self.marca} se ha encendido")
        # Si estaba encendido(true), lo apagamo(false)
        else:
            self.encendido = False
            print(f"El televisor {self.marca} se ha apagado")

    
    def subir_volumen(self):
        if self.encendido:
            self.volumen += 1
            print(f"El volumen actual: {self.volumen}")
        else:
            print("Error: no se puede subir el volumen. El televisor esta apagado... Enciedalo")

tv1 = Televisor("Samsung")

tv1.subir_volumen()
tv1.presionar_boton_encendido()
tv1.subir_volumen()
tv1.subir_volumen()
tv1.presionar_boton_encendido()

class Tienda:
    #Atributo de la clase(APLICA A TODOS)
    impuetro_iva = 0.13

    def __init__(self, productos):
        self.producto = productos

    @classmethod
    def cambiar_impuesto(cls, nuevo_impuesto):
        cls.impuetro_iva = nuevo_impuesto

Tienda.cambiar_impuesto(0.15)


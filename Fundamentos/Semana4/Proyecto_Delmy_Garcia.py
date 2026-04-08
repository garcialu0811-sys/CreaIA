#       Proyecto Final 

producto = ["Fertilizante", "Insecticida", "Herbicida"]

preoductos =[0, 0, 0,]

def promedio_por_lote(productos):
    print("")


def total_unidades_por_lotes():
    for unidades_lotes in producto:
        if unidades_lotes >= 0 | unidades_lotes <= 99:
            print("Insuficiente")
        elif unidades_lotes >= 100 | unidades_lotes <= 299:
            print("Regular")
        elif unidades_lotes >= 300 | unidades_lotes <= 599:
            print("Idóneo")
        elif unidades_lotes >= 600 | unidades_lotes <= 999:
            print("Sobreproducción")

print(f'{"Producto":^15}{"Lotes":^15}{"Total unidades":^15}{"Prom. por lote":^15}{"Categoria":^15}')
print(f'{"Fertilizante":^15}')
print(f'{"Insecticida":^15}')
print(f'{"Herbicida":^15}')

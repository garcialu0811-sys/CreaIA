print("Bienvenido a la tienda")

#Datos del cliente
cliente_vip = False
articulos_comprados =6
dia_semana ="Lunes"

#Regla 1: Descuento mayosita si compra mas de 5 articulos y es VIP
aplica_mayorista = (articulos_comprados > 5) and (cliente_vip == True)
print(f"¿Aplica descuento mayorista? {aplica_mayorista}")

#Regla 2: Descuento especioa de lunes su es lunes o es VIP
descuento = (dia_semana == "Lunes") or (cliente_vip == True)
print(f"¿Aplica descuento especial? {descuento}")

#Regla 3: Verificar que la tienda no este cerrada
tienda_cerrada = False
podemos_vender = not tienda_cerrada
print(f"¿Podemos vender? {podemos_vender}")


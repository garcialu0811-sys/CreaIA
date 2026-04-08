#Ejercicio 1
#Instrucciones:
#Han llegado 47 latas de atún. Queremos acomodarlas en estantes que solo
#soportan 10 latas cada uno. ¿Cuantos estantes llenaremos por completo y cuantas latas nos sobrarán para poner en exhibición?

latas_atun = 47
soporte_estante = 10

estante_lleno = latas_atun // soporte_estante
latas_sobrantes = latas_atun % soporte_estante

print("Estantes llenos: ", estante_lleno)
print("Latas sobrantes: ", latas_sobrantes)





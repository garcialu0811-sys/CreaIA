Limita la cantidad de resultados que quiero obtener de una consulta, es decir, me va a traer solo una cantidad determinada de resultados, aunque existe

-- obtener las primeras 3 filas de la tabla user
SELECT *
FROM users
LIMIT 3;

-- obtener las primeras 2 filas con el name distinto a diego@email.com
SELECT * 
FROM users 
WHERE NOT email = 'diego@gmail.com'
LIMIT 2;
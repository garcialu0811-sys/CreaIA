-- like 
-- significa que le damos un criterio de busqueda a la consulta, y nos va a traer los resultados que cumplan con ese criterio.
-- es un tipo de:
--contiende
-- empieza con
-- termina con



SELECT *
FROM users
WHERE email LIKE '%@gmail.com';

SELECT *
FROM users
WHERE email LIKE 'd%';


-- listar todos los apellidos distintos que existan en la tabla usuarios
SELECT DISTINCT lastname
FROM users; 

-- el nombre, apellido y edad de todos los usuarios que tenfan más de 20 años, ordenados de forma descendente
SELECT name, lastname, age
FROM users
WHERE age > 20
ORDER BY age DESC;


-- user_id y el name de aquellos usuarios que tengan un correo de "@gmail.com" y cuya fecha de inicio (init_date) sea posterior al año 2022
SELECT user_id, name
FROM users
WHERE email 
LIKE '%@gmail.com' 
AND init_date > '2022-12-31';

-- user_id y el name de aquellos usuarios que tengan un correo de "@gmail.com" y cuya fecha de inicio (init_date) sea posterior al año 2022
SELECT user_id, name
FROM users
WHERE email 
LIKE '%@gmail.com' 
AND year(init_date) > 2022;


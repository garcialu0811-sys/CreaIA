-- forma 1
-- acotar los resultados, limitando cual es el criterio de seleccion
    -- que datos queremos
    -- de que tabla
    -- bajo que condiciones

SELECT * FROM users WHERE age > 30;

-- forma 2
SELECT
FROM users
WHERE age > 30;

igual =
difernte != / <>
mayor >
menor <
mayor o igual >=
menor o igual <=

-- solo nombre de la tabla de usuarios con la edad igual a 20
SELECT name FROM users WHERE age = 20;

SELECT name 
FROM users 
WHERE age = 20;


-- filtar todas las edades distintas de la tabla usuarios con edad igual a 22


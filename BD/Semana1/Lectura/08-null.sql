-- NULL
-- 1. todos los usuarios con el correo null
SELECT *
FROM users
WHERE email IS NULL;

-- 2. todos los usuarios con el correo no null
SELECT *
FROM users
WHERE email IS NOT NULL;

-- 3. todos los usuarios con el correo no null y la edad mayor a 25
SELECT *
FROM users
WHERE email IS NOT NULL AND age > 25;

-- 4. ifnull
-- es una funcion que  me va a permitir reemplazar el valor nulo por otro valor que yo le indique
-- obtener el nombre, apellido, y edad de la tabla users y si la edad es nula, remplazarla por 0
SELECT name, lastname, IFNULL(age, 0) AS age
FROM users;

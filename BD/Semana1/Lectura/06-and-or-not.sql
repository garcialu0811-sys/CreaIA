NOT
AND
OR


-- 1. NOT todos los emails que no sean igual a Diego
SELECT * 
FROM users 
WHERE NOT email = 'diego@gmail.com'

-- 2. AND todos los usuarios con email distintos a diego@gmail.com y que tengan edad igual a 15
SELECT * 
FROM users 
WHERE NOT email = 'diego@gmail.com' AND age = 15

--3. OR todos los usuarios con email distintos a diego@gmail.com o que tengan edad igual a 15
SELECT * 
FROM users 
WHERE NOT email = 'diego@gmail.com' OR age = 15
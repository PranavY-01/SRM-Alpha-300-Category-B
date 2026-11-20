/*  PostgreSQL and DBMS Training | Udemy Course 
----------------------------------------------------------------------------------------------
    Section 9. Subqueries
----------------------------------------------------------------------------------------------
*/ 

-- A. Using Subqueries in the SELECT Statement

SELECT name, price FROM products
WHERE price > (SELECT AVG(price) FROM products);

SELECT name, price FROM products
WHERE price > (
    SELECT MAX (price) FROM products
    WHERE department = 'Food'
);

-- B. Using inside SELECT statement

SELECT name, price, (
    SELECT MAX(price) FROM products
) AS max_price  

FROM products
WHERE price > (
    SELECT AVG(price) FROM products
);

-- C. Subqueries in the JOIN Statement

SELECT first_name FROM users
JOIN (
    SELECT user_id FROM orders WHERE product_id = 3
) AS o
ON o.user_id = users.id;

-- D. Subqueries in the WHERE Statement

SELECT id FROM orders
WHERE product_id IN (
    SELECT id FROM products WHERE price / weight > 50
);

-- E. Using NOT IN with Subqueries with LIST

SELECT name, department
FROM products
WHERE department NOT IN (
    SELECT department FROM products WHERE price < 100
);

-- F. Using SOME with Subqueries

SELECT name, department, price
FROM products
WHERE price > SOME (
    SELECT price
    FROM products
    WHERE department = 'Industrial'
);

----------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------
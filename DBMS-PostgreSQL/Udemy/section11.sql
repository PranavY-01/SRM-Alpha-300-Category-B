/*  PostgreSQL and DBMS Training | Udemy Course 
----------------------------------------------------------------------------------------------
    Section 11. Utility Operators, Keywords and Functions 
----------------------------------------------------------------------------------------------
*/ 

-- A. The GREATEST Operator

SELECT GREATEST(10, 20, 30, 40, 50);

SELECT name, weight, GREATEST (30, 2 * weight) FROM products;

-- B. The LEAST Operator

SELECT LEAST(10, 20, 30, 40, 50);

SELECT name, price, LEAST (price * 0.5, 400) FROM products;

-- C. Using CASE Expressions

SELECT name, price, 
    CASE 
        WHEN price < 100 THEN 'Cheap'
        WHEN price >= 100 AND price < 500 THEN 'Medium'
        ELSE 'Expensive'
    END AS price_category
FROM products;

----------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------
/*  PostgreSQL and DBMS Training | Udemy Course 
----------------------------------------------------------------------------------------------
    Section 7. Sorting Records
----------------------------------------------------------------------------------------------
*/ 

CREATE TABLE products (
  id SERIAL PRIMARY KEY,
  name VARCHAR(50),
  department VARCHAR(50),
  price DECIMAL(10,2),
  weight INTEGER
);

INSERT INTO products (id, name, department, price, weight)
VALUES
        (1, 'Shirt', 'Clothing', 19.99, 2),
        (2, 'Towel', 'Home & Garden', 29.99, 3),
        (3, 'Bacon', 'Food', 9.99, 1),
        (4, 'Ball', 'Home & Garden', 14.99, 2),
        (5, 'Fish', 'Food', 24.99, 4),
        (6, 'Mouse', 'Electronics', 34.99, 5),
        (7, 'Computer', 'Electronics', 39.99, 1),

-- A. Basic Sorting

SELECT * FROM products
ORDER BY price;

SELECT * FROM products
ORDER BY price DESC;

-- B. Two Variations of Sorting

SELECT * FROM products
ORDER BY price, weight;

SELECT * FROM products
ORDER BY price, weight DESC;

-- C. Using OFFSET and LIMIT

SELECT * FROM products
OFFSET 2;

SELECT * FROM products
LIMIT 2;

SELECT * FROM products
ORDER BY price DESC
OFFSET 3 LIMIT 2;

----------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------
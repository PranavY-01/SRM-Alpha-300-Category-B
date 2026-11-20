/*  PostgreSQL and DBMS Training | Udemy Course 
----------------------------------------------------------------------------------------------
    Section 8. Unions and Intersections
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
        (7, 'Computer', 'Electronics', 39.99, 1);

-- A. Using UNION

(
    SELECT id, name, department, price, weight
    FROM products
    ORDER BY price DESC
    LIMIT 4
)
UNION
(
    SELECT id, name, department, price, weight
    FROM products
    ORDER BY price / weight DESC
    LIMIT 4
);

(
    SELECT id, name, department, price, weight
    FROM products
    ORDER BY price DESC
    LIMIT 4
)
UNION ALL
(
    SELECT id, name, department, price, weight
    FROM products
    ORDER BY price / weight DESC
    LIMIT 4
);

-- B. Using INTERSECT

(
    SELECT id, name, department, price, weight
    FROM products
    ORDER BY price DESC
    LIMIT 4
)
INTERSECT ALL
(
    SELECT id, name, department, price, weight
    FROM products
    ORDER BY price / weight DESC
    LIMIT 4
);

-- C. Using EXCEPT

(
    SELECT id, name, department, price, weight
    FROM products
    ORDER BY price DESC
    LIMIT 4
)
EXCEPT ALL
(
    SELECT id, name, department, price, weight
    FROM products
    ORDER BY price / weight DESC
    LIMIT 4
);

----------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------
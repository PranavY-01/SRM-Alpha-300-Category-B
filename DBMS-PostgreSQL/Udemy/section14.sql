/*  PostgreSQL and DBMS Training | Udemy Course 
----------------------------------------------------------------------------------------------
    Section 14. Database Validation and Constraints
----------------------------------------------------------------------------------------------
*/ 

-- Note: section 12, 13 are not included because they're not relevant to code-along or to  complex queries.

-- A. Validation and Constraints

SELECT * FROM products;

SELECT * FROM products HAVING price > 100;

-- B. NULL Constraints

SELECT * FROM products WHERE price IS NULL;

SELECT * FROM products ORDER BY price DESC NULLS FIRST;

-- C. Unique Constraints on Row-level Validation

ALTER TABLE products ADD CONSTRAINT unique_product_name UNIQUE (name);

-- D. Multi-column Unique Constraints

ALTER TABLE products ADD CONSTRAINT unique_product_name_department UNIQUE (name, department);

------------------------------------------------------------------------------
------------------------------------------------------------------------------
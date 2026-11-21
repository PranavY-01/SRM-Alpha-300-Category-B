/*  PostgreSQL and DBMS Training | Udemy Course 
----------------------------------------------------------------------------------------------
    Section 17. Build 'Mention' System with Functions and Operators
----------------------------------------------------------------------------------------------
*/ 

-- A. Adding Functions and Operators

SELECT COALESCE(10,5);
SELECT COALESCE((4)::BOOLEAN :: INTEGER,0);

CREATE FUNCTION get_product_price(p_id INT) RETURNS NUMERIC AS $$   
    SELECT COALESCE(price, 0) FROM products WHERE id = p_id;
$$ LANGUAGE SQL;

-- B. Using Functions and Operators

SELECT get_product_price(1);

SELECT get_product_price(100);

SELECT * FROM products WHERE price IS NULL;

-- C. Using Functions and Operators in Queries

SELECT * FROM products WHERE price IS NULL OR get_product_price(id) > 100;

------------------------------------------------------------------------------
------------------------------------------------------------------------------
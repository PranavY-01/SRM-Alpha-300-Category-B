/*  PostgreSQL and DBMS Training | Udemy Course 
----------------------------------------------------------------------------------------------
    Section 16. Functions and Operators
----------------------------------------------------------------------------------------------
*/ 

-- A. Validation and Constraints

SELECT COALESCE(10,5);
SELECT COALESCE((4)::BOOLEAN :: INTEGER,0);
SELECT (NULL)::BOOLEAN::INTEGER

-- B. NULL Constraints

CREATE FUNCTION get_product_price(p_id INT) RETURNS NUMERIC AS $$   
    SELECT COALESCE(price, 0) FROM products WHERE id = p_id;
$$ LANGUAGE SQL;

-- C. Unique Constraints on Row-level Validation

SELECT get_product_price(1);    
AND
SELECT get_product_price(100);

------------------------------------------------------------------------------
------------------------------------------------------------------------------
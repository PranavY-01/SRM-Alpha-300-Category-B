/*  PostgreSQL and DBMS Training | Udemy Course 
----------------------------------------------------------------------------------------------
    Section 10. Selecting Distinct Values
----------------------------------------------------------------------------------------------
*/ 

-- A. Using DISTINCT in the SELECT Statement

SELECT DISTINCT department FROM products;

SELECT DISTINCT department, name FROM products;

SELECT COUNT(DISTINCT department) FROM products;

----------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------
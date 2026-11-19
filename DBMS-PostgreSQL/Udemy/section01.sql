/*  PostgreSQL and DBMS Training | Udemy Course 
----------------------------------------------------------------------------------------------
    Section 1: Basic SQL Commands
----------------------------------------------------------------------------------------------
*/ 

-- A. Create Table

CREATE TABLE cities (
    name VARCHAR(50),
    country VARCHAR(50),
    population INTEGER,
    area INTEGER

);

-- B. Insert Data into Table

INSERT INTO cities (name, country, population, area)
VALUES ('Tokyo', 'Japan', 38505000, 8223),
       ('Delhi', 'India', 28125000, 2240),
       ('Shanghai','China', 22125000, 4015),
       ('Sao Paulo', 'Brazil', 20935000, 3043);

-- C. Retrieve Data from Table

SELECT * from cities;
SELECT name, country FROM cities;
SELECT name, name, name from cities;

-- D. Calculated Column 

SELECT name, population / area FROM cities;  
SELECT name, population / area AS populationDensity FROM cities;    

-- E. String Operations

-- i. Join Using Double Pipe method '||'
SELECT name || ', ' || country AS location FROM cities;

-- ii. Join Using CONCAT() method
SELECT CONCAT(name, ', ', country) AS location FROM cities;

-- iii. LOWER() and UPPER() methods
SELECT LOWER(name) AS lowerCaseName, UPPER(name) AS upperCaseName FROM cities;

--iv. LENGTH() method
SELECT name, LENGTH(name) AS nameLength FROM cities;

----------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------
/*  PostgreSQL and DBMS Training | Udemy Course 
----------------------------------------------------------------------------------------------
    Section 2: Filtering Records
----------------------------------------------------------------------------------------------
*/ 

CREATE TABLE cities (
    name VARCHAR(50),
    country VARCHAR(50),
    population INTEGER,
    area INTEGER

);

INSERT INTO cities (name, country, population, area)
VALUES ('Tokyo', 'Japan', 38505000, 8223),
       ('Delhi', 'India', 28125000, 2240),
       ('Shanghai','China', 22125000, 4015),
       ('Sao Paulo', 'Brazil', 20935000, 3043),
       ('New York', 'USA', 18804000, 783.8),
       ('Mexico City', 'Mexico', 21581000, 1485),
       ('Beijing', 'China', 19618000, 16411);

-- A. Using WHERE Clause

SELECT name, area FROM cities WHERE area > 4000;
SELECT name, area FROM cities WHERE area < 4000;

SELECT name, area FROM cities WHERE area BETWEEN 4000 AND 10000;

SELECT name, area FROM cities WHERE area IN ('Delhi', 'Shanghai', 'Sao Paulo');
SELECT name, area FROM cities WHERE area NOT IN (2240, 4015, 3043);

SELECT name, area FROM cities WHERE area NOT IN (2240, 4015, 3043) AND population > 20000000;
SELECT name, area FROM cities WHERE area NOT IN (2240, 4015, 3043) OR population < 20000000;

-- B. Update Data

UPDATE cities
SET population = 39505000
WHERE name = 'Tokyo';

--C. Delete Data

DELETE FROM cities
WHERE name = 'Tokyo';

----------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------
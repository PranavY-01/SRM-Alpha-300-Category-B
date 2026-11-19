/*  PostgreSQL and DBMS Training | Udemy Course 
----------------------------------------------------------------------------------------------
    Section 3. Working with Tables
----------------------------------------------------------------------------------------------
*/ 


-- A. Schemas

/*
    1. One-to-One
    2. One-to-Many
    3. Many-to-One
    4. Many-to-Many
*/

-- B. Keys

/*
    1. Primary Key - Uniquely identifies a record in a table
    2. Foreign Key - Identifies a record (usually in another table) that the row is associated with
*/

CREATE TABLE users(
    id SERIAL PRIMARY KEY,
    username VARCHAR(50)
);

INSERT INTO users (username)
VALUES
    ('monahan93'),
    ('pferrer'),
    ('si93onis'),
    ('99stroman');

SELECT * from users;

CREATE TABLE photos
    (
        id SERIAL PRIMARY KEY,
        url VARCHAR(200),
        user_id INTEGER REFERENCES users(id)
    );

INSERT INTO photos (url, user_id)
VALUES
    ('http://one.jpg', 4);

SELECT * FROM photos;

-- C. Running Queries on Associated Data

INSERT INTO photos (url, user_id)
VALUES
    ('http://two.jpg', 1),
    ('http://25.jpg', 1),
    ('http://36.jpg', 1),
    ('http://754.jpg', 2),
    ('http://35.jpg', 3),
    ('http://256.jpg', 4);

SELECT * FROM photos;

-- D. Filtering Data on Associated Tables

SELECT * FROM photos
WHERE user id = 4;

-- E. Joining Tables

SELECT url, username FROM photos
JOIN users ON users.id = photos.user_id;

-- F. Handling NULL Values

INSERT INTO photos (url, user_id)
VALUES ('http://jpg', NULL);

SELECT * FROM photos;

----------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------
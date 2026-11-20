/*  PostgreSQL and DBMS Training | Udemy Course 
----------------------------------------------------------------------------------------------
    Section 5. Aggregation of Records
----------------------------------------------------------------------------------------------
*/ 

-- A.Basic Aggregation Functions

CREATE TABLE comments (
  id SERIAL PRIMARY KEY,
  contents VARCHAR(240),
  user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
  photo_id INTEGER REFERENCES photos(id) ON DELETE CASCADE
);

SELECT MAX(id) FROM comments;
SELECT MIN(id) FROM comments;
SELECT AVG(id) FROM comments;
SELECT SUM(id) FROM comments;
SELECT COUNT(id) FROM comments;

-- B. With GROUP BY Clause

SELECT user_id FROM comments GROUP BY user_id;

-- C. With HAVING Clause

SELECT photo_id,COUNT(*)
FROM comments
WHERE photo_id<3
GROUP BY photo_id
HAVING COUNT(*)>2;

-- D. With ORDER BY Clause

SELECT photo_id,COUNT(*)
FROM comments
WHERE photo_id<3
GROUP BY photo_id
ORDER BY COUNT(*) DESC;

----------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------
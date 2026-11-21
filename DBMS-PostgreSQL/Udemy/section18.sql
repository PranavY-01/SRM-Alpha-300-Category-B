/*  PostgreSQL and DBMS Training | Udemy Course 
----------------------------------------------------------------------------------------------
    Section 17. Build 'Hashtag' System
----------------------------------------------------------------------------------------------
*/ 

-- A. Designing the Hashtag System

CREATE TABLE hashtags (
    id SERIAL PRIMARY KEY,
    tag VARCHAR(50) UNIQUE NOT NULL
);

CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    content TEXT NOT NULL
    user_id INT REFERENCES users(id) ON DELETE CASCADE
);

SELECT * FROM posts WHERE content LIKE '%#%';

-- B. Extracting Hashtags from Posts

SELECT content, regexp_matches(content, '#(\w+)') AS hashtags
FROM posts;

SELECT content, unnest(regexp_matches(content, '#(\w+)', 'g')) AS hashtags
FROM posts;

------------------------------------------------------------------------------
------------------------------------------------------------------------------
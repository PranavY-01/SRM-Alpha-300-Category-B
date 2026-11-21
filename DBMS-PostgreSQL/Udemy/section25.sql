/*  PostgreSQL and DBMS Training | Udemy Course 
----------------------------------------------------------------------------------------------
    Section 25. Advanced Query Techniques
----------------------------------------------------------------------------------------------
*/ 

-- Section 22, 23 and 24 are not included.

-- A. Adding Data

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id) ON DELETE CASCADE,
    title VARCHAR(200) NOT NULL,
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE comments (
    id SERIAL PRIMARY KEY,
    post_id INT REFERENCES posts(id) ON DELETE CASCADE,
    user_id INT REFERENCES users(id) ON DELETE CASCADE,
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO users (name, email)
VALUES
    ('Alice', 'alice@example.com'),
    ('Bob', 'bob@example.com'),
    ('Charlie', 'charlie@example.com'),
    ('David', 'david@example.com'),
    ('Eve', 'eve@example.com'),
    ('Frank', 'frank@example.com');

INSERT INTO posts (user_id, title, content)
VALUES
    (1, 'Post by Alice', 'Content of Alice''s post'),
    (2, 'Post by Bob', 'Content of Bob''s post'),
    (1, 'Another post by Alice', 'Content of Alice''s second post'),
    (3, 'Post by Charlie', 'Content of Charlie''s post'),
    (4, 'Post by David', 'Content of David''s post'),
    (5, 'Post by Eve', 'Content of Eve''s post');

INSERT INTO comments (post_id, user_id, content)
VALUES
    (1, 2, 'Comment by Bob on Alice''s post'),
    (1, 3, 'Comment by Charlie on Alice''s post'),
    (2, 1, 'Comment by Alice on Bob''s post'),
    (3, 2, 'Comment by Bob on Alice''s second post'),
    (4, 1, 'Comment by Alice on David''s post'),
    (5, 6, 'Comment by Frank on Eve''s post');

-- B. Calculating Cost of Comments per User

SELECT u.name AS user_name, COUNT(c.id) AS comment_count, COUNT(c.id) * 0.05 AS total_cost
FROM users u
LEFT JOIN comments c ON u.id = c.user_id
GROUP BY u.id, u.name 
AS user_name, comment_count, total_cost;

CREATE VIEW user_comment_cost AS
SELECT u.name AS user_name, COUNT(c.id) AS comment_count, COUNT(c.id) * 0.05 AS total_cost
FROM users u
LEFT JOIN comments c ON u.id = c.user_id
GROUP BY u.id, u.name;

------------------------------------------------------------------------------
------------------------------------------------------------------------------
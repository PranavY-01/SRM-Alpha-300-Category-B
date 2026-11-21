/*  PostgreSQL and DBMS Training | Udemy Course 
----------------------------------------------------------------------------------------------
    Section 21. Approaching Complex Queries
----------------------------------------------------------------------------------------------
*/ 

-- A. Adding Data

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id) ON DELETE CASCADE,
    content TEXT NOT NULL
);

CREATE TABLE comments (
    id SERIAL PRIMARY KEY,
    post_id INT REFERENCES posts(id) ON DELETE CASCADE,
    user_id INT REFERENCES users(id) ON DELETE CASCADE,
    content TEXT NOT NULL
);

INSERT INTO users (name)
VALUES
    ('Alice'),
    ('Bob'),
    ('Charlie'),
    ('David');

INSERT INTO posts (user_id, content)
VALUES
    (1, 'Post by Alice'),
    (2, 'Post by Bob'),
    (1, 'Another post by Alice'),
    (3, 'Post by Charlie'),
    (4, 'Post by David');

INSERT INTO comments (post_id, user_id, content)
VALUES
    (1, 2, 'Comment by Bob on Alice''s post'),
    (1, 3, 'Comment by Charlie on Alice''s post'),
    (2, 1, 'Comment by Alice on Bob''s post'),
    (3, 2, 'Comment by Bob on Alice''s second post'),
    (4, 1, 'Comment by Alice on David''s post');

-- B. Complex Queries

SELECT u.name AS user_name, p.content AS post_content, c.content AS comment_content
FROM users u
JOIN posts p ON u.id = p.user_id
LEFT JOIN comments c ON p.id = c.post_id
INNER JOIN users cu ON c.user_id = cu.id
WHERE u.name = 'Alice';

SELECT u.name AS user_name, p.content AS post_content, c.content AS comment_content
FROM users u
JOIN posts p ON u.id = p.user_id
RIGHT JOIN comments c ON p.id = c.post_id
INNER JOIN users cu ON c.user_id = cu.id
WHERE cu.name = 'Bob';

-- C. Posts by Particular Users with Comments

CREATE FUNCTION get_user_posts_with_comments(p_user_id INT) RETURNS TABLE(post_content TEXT, comment_content TEXT) AS $$
BEGIN
    RETURN QUERY
    SELECT p.content, c.content
    FROM posts p
    LEFT JOIN comments c ON p.id = c.post_id
    WHERE p.user_id = p_user_id;
END;

$$ LANGUAGE plpgsql;

------------------------------------------------------------------------------
------------------------------------------------------------------------------
/*  PostgreSQL and DBMS Training | Udemy Course 
----------------------------------------------------------------------------------------------
    Section 20. Database Design Patterns
----------------------------------------------------------------------------------------------
*/ 

-- Section 19 is not included because it's not relevant to code-along or to complex queries.

-- A. Database Design Patterns

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);

INSERT INTO users (name, email) 
VALUES
    ('Alice', 'alice@example.com'),
    ('Bob', 'bob@example.com'),
    ('Charlie', 'charlie@example.com');

-- B. One-to-Many Relationship

CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id) ON DELETE CASCADE,
    content TEXT NOT NULL
);

INSERT INTO posts (user_id, content)
VALUES
    (1, 'Post by Alice'),
    (2, 'Post by Bob'),
    (1, 'Another post by Alice');

-- C. Many-to-Many Relationship

CREATE TABLE tags (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL
);

CREATE TABLE post_tags (
    post_id INT REFERENCES posts(id) ON DELETE CASCADE,
    tag_id INT REFERENCES tags(id) ON DELETE CASCADE,
    PRIMARY KEY (post_id, tag_id)
);

INSERT INTO tags (name)
VALUES
    ('tag1'),
    ('tag2'),
    ('tag3');

INSERT INTO post_tags (post_id, tag_id)
VALUES
    (1, 1),
    (1, 2),
    (2, 2),
    (3, 3);

------------------------------------------------------------------------------
------------------------------------------------------------------------------
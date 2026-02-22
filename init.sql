-- init.sql
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    age INTEGER
);

INSERT INTO users (name, age) VALUES ('Alice', 30), ('Bob', 25);
--Create database api
CREATE DATABASE api;

--Use db api
\c api

--Create tables users
CREATE TABLE IF NOT EXISTS public.users
(
    id bigserial PRIMARY KEY,
    first_name VARCHAR(20)  NOT NULL,
    last_name VARCHAR(20) NOT NULL,
    birthday date,
    gender VARCHAR(20) NOT NULL,
    hobby text,
    city VARCHAR(30),
    password VARCHAR(80),
    login VARCHAR(20),
    is_admin boolean DEFAULT false
);

--Add first test record
INSERT INTO users(id, first_name, last_name, birthday, gender, hobby, city)
    SELECT 1, 'first', 'user', '1990-01-01', 'male', 'testing', 'testcity'
WHERE NOT EXISTS(
    SELECT NULL FROM users
        WHERE (first_name, last_name, birthday, gender, hobby, city) =
        ('first', 'user', '1990-01-01', 'male', 'testing', 'testcity')
);

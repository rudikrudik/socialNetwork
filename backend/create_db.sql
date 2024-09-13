--Create database api
CREATE DATABASE api;

--Use db api
\c api

--Create tables users
CREATE TABLE IF NOT EXISTS public.users
(
    id bigserial PRIMARY KEY,
    first_name VARCHAR(20),
    last_name VARCHAR(20),
    birthday date,
    gender VARCHAR(20),
    hobby text,
    city VARCHAR(30),
    password VARCHAR(80) NOT NULL,
    login VARCHAR(20) NOT NULL,
    is_admin boolean DEFAULT false
);

--Add first test record
INSERT INTO users(id, first_name, last_name, birthday, gender, hobby, city, password, login)
    SELECT 1, 'first', 'user', '1990-01-01', 'male', 'testing', 'city', 'password', 'login'
WHERE NOT EXISTS(
    SELECT NULL FROM users
        WHERE (first_name, last_name, birthday, gender, hobby, city, password, login) =
        ('first', 'user', '1990-01-01', 'male', 'testing', 'city', 'password', 'login')
);
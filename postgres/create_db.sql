--Add pg stat
CREATE EXTENSION IF NOT EXISTS pg_stat_statements;

--Create database api
CREATE DATABASE api;

--Use db api
\c api

--Create tables users
CREATE TABLE IF NOT EXISTS public.users
(
    id bigserial PRIMARY KEY,
    first_name VARCHAR(30),
    last_name VARCHAR(30),
    birthday date,
    gender VARCHAR(20),
    hobby text,
    city VARCHAR(40),
    password VARCHAR(80) NOT NULL,
    login VARCHAR(30) NOT NULL,
    avatar text,
    is_admin boolean DEFAULT false
);

CREATE TABLE public.user_posts
(
	id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    post_date_create timestamp,
    post_content text,
    post_images text,
    post_likes text,
    FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
);

CREATE TABLE public.user_friends
(
    user_id INTEGER NOT NULL,
	friend_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
);

--Add first test record
INSERT INTO users(id, first_name, last_name, birthday, gender, hobby, city, password, login)
    SELECT 1, 'first', 'user', '1990-01-01', 'male', 'testing', 'city', 'password', 'login'
WHERE NOT EXISTS(
    SELECT NULL FROM users
        WHERE (first_name, last_name, birthday, gender, hobby, city, password, login) =
        ('first', 'user', '1990-01-01', 'male', 'testing', 'city', 'password', 'login')
);
-- Run this once against your MySQL server to set up the database.
CREATE DATABASE IF NOT EXISTS student_management;
USE student_management;

CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE,
    course VARCHAR(100) NOT NULL
);

-- Sample records
INSERT IGNORE INTO students (name, email, course) VALUES
    ('Ananya Rao', 'ananya.rao@example.com', 'B.Tech AI & DS'),
    ('Karthik Iyer', 'karthik.iyer@example.com', 'B.Tech CSE'),
    ('Sneha Menon', 'sneha.menon@example.com', 'B.Tech ECE'),
    ('Rahul Varma', 'rahul.varma@example.com', 'B.Tech Mechanical'),
    ('Divya Prakash', 'divya.prakash@example.com', 'B.Tech IT');

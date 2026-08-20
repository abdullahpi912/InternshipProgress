CREATE DATABASE IF NOT EXISTS student_management;
USE student_management;

CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE,
    course VARCHAR(150) NOT NULL
);

INSERT INTO students (name, email, course) VALUES
('Abdullah', 'abdullah@example.com', 'B.Tech AI & DS'),
('Aisha', 'aisha@example.com', 'B.Tech CSE'),
('Rahul', 'rahul@example.com', 'B.Tech IT'),
('Priya', 'priya@example.com', 'B.Tech ECE'),
('Mohammed', 'mohammed@example.com', 'B.Tech AI & DS')
ON DUPLICATE KEY UPDATE name = VALUES(name), course = VALUES(course);

SELECT * FROM students ORDER BY id;

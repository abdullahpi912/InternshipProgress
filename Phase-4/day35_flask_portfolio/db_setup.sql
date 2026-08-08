-- Day 35 — Basics of SQL — Innolift Ventures, Crescent Batch
-- Portfolio database setup

DROP DATABASE IF EXISTS portfolio_db;
CREATE DATABASE portfolio_db;
USE portfolio_db;

CREATE TABLE skills (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    category VARCHAR(50),
    proficiency INT
);

CREATE TABLE projects (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    description TEXT,
    tech_stack VARCHAR(200),
    github_url VARCHAR(255),
    demo_url VARCHAR(255)
);

CREATE TABLE certifications (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    issuer VARCHAR(100),
    issue_date DATE,
    credential_url VARCHAR(255)
);

CREATE TABLE messages (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    subject VARCHAR(150),
    message TEXT NOT NULL,
    submitted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO skills (name, category, proficiency) VALUES
('Python', 'Programming', 90),
('SQL', 'Database', 85),
('Power BI', 'Data Analytics', 80),
('Machine Learning', 'AI/ML', 85),
('EDA', 'Data Analytics', 82),
('Flask', 'Backend', 80);

INSERT INTO projects (title, description, tech_stack, github_url) VALUES
('AgriSense', 'Soil & weather-based crop recommendation app', 'React, Flask, ML', 'https://github.com/abdullahpi912/agrisense'),
('Portfolio Website', 'Personal portfolio showcasing projects, skills and certifications', 'HTML, CSS, JS, Flask', 'https://github.com/abdullahpi912/portfolio'),
('Internship Progress Tracker', 'Daily assignments and progress log for Crescent Batch 1 internship at Innolift Ventures', 'Python, SQL, Flask, React', 'https://github.com/abdullahpi912/InternshipProgress');

INSERT INTO certifications (title, issuer, issue_date) VALUES
('Python for Data Science', 'Coursera', '2025-06-10'),
('Machine Learning Foundations', 'Udemy', '2025-09-22'),
('SQL Basics', 'HackerRank', '2026-01-15');

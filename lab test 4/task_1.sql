-- Create Database
CREATE DATABASE UniversityExamDB;
USE UniversityExamDB;

-- Create Students table
CREATE TABLE Students (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(50),
    department VARCHAR(50)
);

-- Create Subjects table
CREATE TABLE Subjects (
    subject_id INT PRIMARY KEY,
    subject_name VARCHAR(50),
    max_marks INT
);

-- Create Marks table
CREATE TABLE Marks (
    mark_id INT PRIMARY KEY,
    student_id INT,
    subject_id INT,
    marks_obtained INT,
    FOREIGN KEY (student_id) REFERENCES Students(student_id),
    FOREIGN KEY (subject_id) REFERENCES Subjects(subject_id)
);

-- Insert sample data into Students
INSERT INTO Students (student_id, student_name, department) VALUES
(1, 'Aarav Sharma', 'Computer Science'),
(2, 'Diya Patel', 'Information Technology'),
(3, 'Rohan Mehta', 'Electronics'),
(4, 'Priya Nair', 'Mechanical'),
(5, 'Karan Singh', 'Civil');

-- Insert sample data into Subjects
INSERT INTO Subjects (subject_id, subject_name, max_marks) VALUES
(101, 'Mathematics', 100),
(102, 'Physics', 100),
(103, 'Chemistry', 100),
(104, 'Computer Science', 100),
(105, 'English', 100);

-- Insert sample data into Marks
INSERT INTO Marks (mark_id, student_id, subject_id, marks_obtained) VALUES
(1, 1, 101, 90),
(2, 1, 102, 92),
(3, 1, 103, 88),
(4, 1, 104, 94),
(5, 1, 105, 91),

(6, 2, 101, 80),
(7, 2, 102, 75),
(8, 2, 103, 89),
(9, 2, 104, 78),
(10, 2, 105, 84),

(11, 3, 101, 86),
(12, 3, 102, 88),
(13, 3, 103, 82),
(14, 3, 104, 90),
(15, 3, 105, 87),

(16, 4, 101, 70),
(17, 4, 102, 68),
(18, 4, 103, 72),
(19, 4, 104, 65),
(20, 4, 105, 69),

(21, 5, 101, 95),
(22, 5, 102, 96),
(23, 5, 103, 94),
(24, 5, 104, 97),
(25, 5, 105, 93);

-- Query to find students scoring above 85% in all subjects
SELECT s.student_id, s.student_name
FROM Students s
JOIN Marks m ON s.student_id = m.student_id
JOIN Subjects sub ON m.subject_id = sub.subject_id
GROUP BY s.student_id, s.student_name
HAVING MIN((m.marks_obtained * 100.0 / sub.max_marks)) > 85;

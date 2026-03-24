

-- Subqueries in MySQL
-- A subquery is a query nested inside another SQL query.
-- It helps you perform complex filtering, calculations, or temporary data shaping by breaking down the logic into smaller steps.

-- You can use subqueries in SELECT, FROM, or WHERE clauses.


-- ---------

-- When to Use Subqueries :
--  \  When your logic depends on calculated values (like averages or counts)
--   \ When you need to filter based on dynamic conditions
--    \ When youre breaking down complex queries for readability


-- When to Avoid Subqueries :
--   \ When the same result can be achieved with a JOIN, which is often faster
--    \ When the subquery is being executed repeatedly for every row (correlated subqueries on large tables)


-- ------------

-- Types of Subqueries :

-- Type	                Description
-- Scalar Subquery	    Returns a single value
-- Row Subquery	        Returns one row with multiple columns
-- Table Subquery       Returns multiple rows and columns
-- Correlated Subquery	Refers to the outer query inside the subquery



-- ===================================


-- 1.  Subquery in the WHERE Clause :
-- Example: student who age more than average

SELECT name, age
FROM student_table
WHERE age > (
    SELECT AVG(age)
    FROM student_table
);


-- =====================================

--  2.  Subquery in the FROM Clause :
-- Example: inner query is the same table , as outer query table 

SELECT StudentID ,Name, City
FROM (
    SELECT StudentID, Name, City  
    FROM students
) AS dept_data;



-- 3. Subquery in the SELECT Clause :
-- Example: Count of alumni per student ( all std alumni_count is 0 since there is no relation btw table

SELECT name,
       (SELECT COUNT(*) FROM alumni 
       WHERE alumni.AlumniID = student_table.roll_no) AS alumni_count
FROM student_table;


-- =============================================


-- Correlated Subqueries :
-- A correlated subquery depends on the outer query. It runs once for each row in the outer query.

-- Example: Student age more than class average

SELECT roll_no ,name, age, admission_date
FROM student_table std
WHERE age > (
    SELECT AVG(age)
    FROM student_table
);

-- We are telling MySQL: For each student, compare their age with the average age of their class.


-- =============================================

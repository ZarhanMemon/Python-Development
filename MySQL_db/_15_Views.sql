

-- Views in MySQL
-- A View in MySQL is like a virtual table. It doesn’t store data by itself 
-- but instead shows data from one or more tables through a saved SQL query.

-- You can use a view just like a regular table: SELECT from it, filter it, join it, etc.


-- Why Use Views?
-- To simplify complex queries by giving them a name.
-- To hide sensitive columns from users.
-- To show only specific rows/columns from a table.
-- To reuse common query logic across your app or reports.


-- ==================================================


-- 1. Creating a View :
 
CREATE VIEW all_students 
AS
SELECT roll_no ,name
FROM student_table;

-- Create a view called all_students that shows  roll_no , name  from the student_table.


-- ----------

-- 2. Using a View :

SELECT * FROM all_students;

SELECT * FROM all_students
WHERE name like 'A%';


-- ----------

-- 3. Updating a View :

CREATE OR REPLACE VIEW all_students     -- now the all_student view table have the alumni student table
AS
SELECT Name, City
FROM alumni;


-- ----------

-- 4. Dropping (Deleting) a View :

DROP VIEW all_students;           -- This removes the view from the database.


-- ======================================================


-- Notes :
--  \ Views don’t store data. If the underlying table changes, the view reflects that automatically.
--  \ Not all views are updatable. Simple views usually are (like those selecting from one table without grouping or joins), but complex ones may not allow INSERT, UPDATE, or DELETE.
--  \ Views can make your queries cleaner and easier to maintain.


-- ------

-- Example Use Case :

-- You have this query used 5 times across your app:
SELECT roll_no, name, age, admission_date
FROM student_table
WHERE  age >= 18  AND age <= 25;


-- Instead of repeating it, just create a view , use it 5 plces by calling select on the view:
CREATE VIEW teen_student 
AS
SELECT roll_no, name, age, admission_date
FROM student_table
WHERE  age >= 18  AND age <= 25;



-- apply the view use where u req that query logic
SELECT * FROM teen_student;
SELECT * FROM teen_student;
SELECT * FROM teen_student;
SELECT * FROM teen_student;
SELECT * FROM teen_student;
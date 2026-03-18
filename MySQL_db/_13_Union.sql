
-- Create first table: Students
CREATE TABLE Students (
    StudentID INT,
    Name VARCHAR(50),
    City VARCHAR(50)
);

-- Insert sample data into Students
INSERT INTO Students (StudentID, Name, City) VALUES
(1, 'Alice', 'Pune'),
(2, 'Bob', 'Mumbai'),
(3, 'Charlie', 'Delhi');

-- Create second table: Alumni
CREATE TABLE Alumni (
    AlumniID INT,
    Name VARCHAR(50),
    City VARCHAR(50)
);

-- Insert sample data into Alumni
INSERT INTO Alumni (AlumniID, Name, City) VALUES
(101, 'David', 'Pune'),
(102, 'Eve', 'Mumbai'),
(103, 'Bob', 'Mumbai'); -- Notice Bob appears in both tables

-- ===========================================================================================================




-- UNION in MySQL
-- The UNION operator is used to combine the result sets of two or more SELECT statements into a single result.

-- It helps when:
-- You're pulling similar data from different tables.
-- You want to merge results from multiple queries into one list.

-- ---------------------

-- Use UNION if:
-- You want a clean list without duplicates.

-- Use UNION ALL if:
-- You want performance and don’t care about duplicates.
-- Or you expect duplicate values and want to preserve them.


-- ==============================

-- 1.  UNION (removes duplicates):

--  RULES ->
--   \ Same number of columns in all SELECT statements.
--   \ Compatible data types in corresponding columns.
--   \ Columns will be matched by position, not by name.

SELECT name, city FROM Alumni      
UNION
SELECT name, city FROM Students;  

-- This will return a distinct list of names and cities across both tables (Bob will appear only once).


-- -------------

-- 2.  UNION ALL (keeps duplicates) : 

SELECT name, city FROM Alumni        -- same rules for Union all as Union
UNION ALL
SELECT name, city FROM Students;  

--  This will return all rows, including duplicates (Bob will appear twice).


-- ==========================================


-- Sorting the Combined Result :-
-- You can sort the final output using ORDER BY at the end:
SELECT name ,  city FROM Alumni
UNION
SELECT name , city FROM Students
ORDER BY name;


-- ==========================================

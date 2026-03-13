

-- Deleting Data from a Table


-- DELETE FROM table_name
-- WHERE condition;

-- DELETE FROM: Specifies the table from which to remove rows.
-- WHERE: Filters which rows should be deleted.

-- --------------------------


-- 1. Delete a Specific Row:
DELETE FROM student
WHERE roll_no = 2;


-- --------------------------

-- 2. Delete Rows Using Comparison Operators:
DELETE FROM student
WHERE age < 16;

-- --------------------------


-- 3. Delete Rows Where a Column is NULL:
DELETE FROM student
WHERE grade IS NULL;

-- --------------------------

-- 4. Delete All Rows (Use with Caution):

TRUNCATE TABLE student; 
--  When you want to delete all data quickly and reset the table, but keep the structure.

DELETE FROM student;
-- This deletes all rows but retains the table structure.


-- --------------------------

-- 5. Completely Remove the Table:
DROP TABLE student;
-- This removes both the data and the table structure.



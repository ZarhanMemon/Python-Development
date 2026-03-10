
-- Alter a Table :-


 -- 1. Change table name:
RENAME TABLE students TO student_table;

-- 2. Dropping a Table:
DROP TABLE students;

-- 3. Renaming a Column:
ALTER TABLE student_table RENAME COLUMN id TO roll_no;

-- 4. Adding a Column:
ALTER TABLE student_table ADD COLUMN new_col INT NOT NULL;

-- 5. Dropping a Column:
ALTER TABLE student_table DROP COLUMN new_col;

-- 6. Modifying a Column:
ALTER TABLE student_table MODIFY COLUMN new_col INT NULL DEFAULT 12;

-- 7. Changing the Sequence of Columns:
ALTER TABLE student_table MODIFY COLUMN new_col INT AFTER name;  -- FIRST

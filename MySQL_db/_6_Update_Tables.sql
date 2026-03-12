

-- Updating Data in a Table


-- UPDATE table_name
-- SET column1 = value1, column2 = value2, ...
-- WHERE condition;

-- UPDATE: Specifies the table you want to modify.
-- SET: Assigns new values to columns.
-- WHERE: Filters which rows should be updated. 



-- 1. Update a Single Row :
UPDATE student
SET grade = '12th'
WHERE roll_no = 2;


-- 2. Update Multiple Columns :
UPDATE student
SET grade = '12th' , name = 'abc', age= 17
WHERE roll_no = 2;



-- 3. Update All Rows :
UPDATE student
SET age = 18;


-- 4. Conditional Update with Comparison Operators :
UPDATE student
SET age = age + 1
WHERE age <= 18;


-- 5. Update Using IS NULL :
UPDATE student
SET grade = 'Unknown'
WHERE grade IS NULL;



SELECT * FROM student; -- verifying ke liye

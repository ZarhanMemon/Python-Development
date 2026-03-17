-- USE school;




-- Joins in MySQL

-- When we have data split across multiple tables, we use joins to combine that data and get the full picture.

-- Condition : Tables are related and  1 Foreign Key 

SELECT * FROM students;   -- students( class_ref_id  ) ->  classes( class_id )
select * from classes;


-- Join Type       	What it does
-- INNER JOIN	     Only rows with a match in both tables
-- LEFT JOIN	    All rows from the left table, with matched data if any
-- RIGHT JOIN	    All rows from the right table, with matched data if any
-- CROSS JOIN	    All combinations of rows from both tables

-- ========================================

-- 1. INNER JOIN : 

SELECT students.roll_no , students.name ,  classes.class_name       -- what to display
FROM
students INNER JOIN classes                                        -- join type on tables
ON students.class_ref_id = classes.class_id;                       -- condition

-- This will show only students who have class recorded. If a student has no class, they will not appear in the result.

 
 -- -----------------

-- 2. LEFT JOIN (or LEFT OUTER JOIN) :

SELECT students.roll_no , students.name ,  classes.class_name      
FROM
students LEFT JOIN classes                                  
ON students.class_ref_id = classes.class_id;       -- Raj -> null  is shown too              

-- We are telling MySQL to include all students, even if they don't have any class. 
-- If there's no match in the CLASSES table, it will show NULL.      


-- ------------------

-- 3. RIGHT JOIN (or RIGHT OUTER JOIN) :

SELECT students.roll_no , students.name ,  classes.class_name      
FROM
students RIGHT JOIN classes                                  
ON students.class_ref_id = classes.class_id;     -- shows all Classes matching withstudent or not  , SHOWS ORDER of Classes table record ARTs -> COMM -> Sci

-- We are telling MySQL to include all rows from the right table (classes),
-- even if the a class is dont selected by any student show it.


-- --------------------

-- 5. CROSS/FULL JOIN  :   give all possible combination of both tables records.

SELECT students.roll_no , students.name ,  classes.class_name      
FROM
students CROSS JOIN classes;                                      -- No condition or else behave like other join

-- We are telling MySQL to combine every row in the first table with every row in the second table.
-- Use this only when you really want all combinations – it can produce a lot of rows.     


-- =====================================================
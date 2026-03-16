CREATE DATABASE school;
USE school;



--  Foreign Keys 
-- This guide demonstrates how to create a database, define tables, and use foreign keys to establish relationships between them.



CREATE TABLE classes (
 class_id INT auto_increment primary key,
 class_name varchar(10) not null
 );
  
 
 CREATE TABLE students (
  roll_no INT auto_increment primary key,
  name varchar(20) not null,
  class_ref_id INT ,
  
  --  Adding a custom constraint ( FOREIGN key ) -> to  the class_ref_id  
  -- class_ref_id in student table ->  so that it ref to the class_id in classes table
  -- TO determin which std is in which class
  CONSTRAINT fk_std_class FOREIGN KEY ( class_ref_id ) 
  REFERENCES classes( class_id )
  
  -- 1. 
  ON DELETE SET NULL     -- -> CASCADE ,  RESTICT
     -- If any class is deleted, the related student  that have it, will have ( class_ref_id ) set to NULL.
     
  -- 2. 
  ON UPDATE CASCADE      --  If a class ID changes, it will update automatically in the students table. 
  );


-- =============================================================================


INSERT INTO classes (class_name) VALUES ('Arts'), ('Science'), ('Commerce');

INSERT INTO students (name, class_ref_id) VALUES 
('Alice', 1),
('Bob', 2),
('Charlie', 1);


-- ===============================================================================

-- 1.  ON DELETE   :-  If any class is deleted, the related student  that have it, will have ( class_ref_id ) set to NULL.

SELECT * FROM classes;      -- Arts , Science , Commerce
SELECT * FROM students;     -- all student pointing to correct records in classes tables

DELETE FROM classes WHERE class_id = 2;  --  Science class deleted

SELECT * FROM classes;     -- Arts ,  null , Commerce
SELECT * FROM students;    --  ALL STUDENT IN CLASS 2 THAT DELETED , NOW REFER TO NULL in classes table


-- Other ( ON DELETE ... ) :- 
-- ON DELETE CASCADE: Deletes the child rows when the parent row is deleted.
-- ON DELETE RESTRICT: Prevents deletion if any child rows exist.
-- ON DELETE NO ACTION: Same as RESTRICT in MySQL.
-- ON DELETE SET DEFAULT: Not supported in MySQL (but available in some other DBMSs).


-- -------------

-- 2.  ON UPDATE CASCADE :- If a class ID changes, it will update automatically in the students table. 

SELECT * FROM classes;      --  1 , 2 , 3
SELECT * FROM students;     -- all student pointing to correct class_id in classes tables

Update classes SET class_id = 5
WHERE class_id = 2;               --  Science class  -> class_id  = 5

SELECT * FROM classes;     -- 1 , 5 , 3
SELECT * FROM students;    --  ALL STUDENT IN CLASS 2 THAT updated to 5  , NOW REFER TO  class_ref_id = 5


-- =======================================================================================


-- View the Relationships :-

SHOW CREATE TABLE students;    -- shows the constraint structure of table

-- To see all foreign keys in the current database:
SELECT 
    table_name, 
    column_name, 
    constraint_name, 
    referenced_table_name, 
    referenced_column_name
FROM 
    information_schema.key_column_usage
WHERE 
    referenced_table_name IS NOT NULL
    AND table_schema = 'school';


-- =======================================================================================



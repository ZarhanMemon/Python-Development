USE my_db;  

-- Creating Tables :

-- CREATE TABLE table_name (
--   column1 datatype constraints,
--   column2 datatype constraints,
--   ...
-- );

CREATE TABLE students (
  id INT PRIMARY KEY,
  name VARCHAR(100) NOT NULL DEFAULT 'abc',
  age INT,
  email VARCHAR(100) UNIQUE,
  admission_date DATE
);

-- id INT PRIMARY KEY         – A unique identifier for each student that auto-increments.
-- name VARCHAR(100) NOT NULL  – Name must be provided.
-- age INT                     – Stores numeric values for age.
-- email VARCHAR(100) UNIQUE     – Each email must be different.
-- admission_date DATE           – Stores the date of admission.


-- =====================

-- Commonly Used Data Types :-

-- 1. INT – Whole numbers (e.g., age, quantity)

-- 2. VARCHAR(n) – Variable-length string of length n (e.g., names, emails)

-- 3. TEXT – Long text strings (e.g., descriptions , meta describe)

-- 4. DATE – Stores date values (YYYY-MM-DD)

-- 5. DATETIME – Stores date and time values

-- 6. BOOLEAN – Stores TRUE or FALSE

-- -------------

-- Common Constraints :-

-- PRIMARY KEY – Uniquely identifies each record
-- NOT NULL – Ensures the column cannot be left empty
-- UNIQUE – Ensures all values in a column are different
-- AUTO_INCREMENT – Automatically increases numeric values
-- DEFAULT "value" – Sets a default value for the column
-- FOREIGN KEY – Enforces relationships between tables


-- ===============


SHOW TABLES; --  give the no of table

DESCRIBE students;  --  give structutere of table student

SELECT * FROM students;  -- return the table with its data
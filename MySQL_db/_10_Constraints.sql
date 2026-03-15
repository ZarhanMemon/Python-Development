

-- Constraints 

-- Constraints in SQL are rules applied to table columns to enforce data integrity, consistency, and validity. 
-- They restrict the type of data that can be inserted into a table and help prevent invalid or duplicate entries.

-- Why Use Constraints?
--   > Ensure data quality and reliability
--   > Prevent invalid, duplicate, or null data
--   > Maintain business rules directly in the database layer


-- Constraint		Purpose 
-- NOT NULL 		Disallow null values	 
-- UNIQUE			Disallow duplicate values	 
-- DEFAULT			Set default value if none given	 
-- CHECK			Enforce value conditions	 
-- CONSTRAINT ...   For creating a named constraint by using all other contn help

-- --------------------------

-- 1. NOT NULL :

CREATE TABLE employees (
    id INT NOT NULL,
    name VARCHAR(100) NOT NULL    -- ensure column cannot have null values
);

-- --------------------------

-- 2. UNIQUE :

CREATE TABLE users (
    username VARCHAR(50) UNIQUE,   -- ensure each row have unique valu of the column
    email VARCHAR(100) UNIQUE
);

-- Note: A table can have multiple UNIQUE constraints, but only one PRIMARY KEY.

-- --------------------------

-- 3. DEFAULT "_" :

-- Sets a default value for a column if none is provided during insert.

CREATE TABLE products (
    name VARCHAR(100),
    status VARCHAR(20) DEFAULT 'in_stock'
);

-- ----------------------------

-- 4. CHECK ( .. ) :

-- Validates that values in a column meet a specific condition before inserting it.

CREATE TABLE accounts (
    id INT,
    balance DECIMAL(10,2) CHECK (balance >= 0)
);

-- ----------------------------

-- 5. Naming Constraints :

--  You can give explicit names to constraints. 
--  This makes them easier to reference, especially when altering or dropping them later.

CREATE TABLE students (
    roll_no INT PRIMARY KEY,
    age INT CONSTRAINT chk_age CHECK (age >= 5), 
    email VARCHAR(100) UNIQUE
);

-- Benefits of Named Constraints:
--  \ Improves clarity and debugging
--  \ Useful when using ALTER TABLE to drop constraints
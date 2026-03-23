


-- Indexes in MySQL

-- An index in MySQL is a data structure that makes data retrieval faster—especially
--  when you're using WHERE, JOIN, ORDER BY, or searching large tables.


-- ------------

-- Why Use Indexes?
--  \ Speed up queries that search, filter, or sort data.
--  \ Improve performance for frequent lookups or joins.
--  \ Enhance scalability of your database over time.

-- ---------


-- Action	        Syntax Example
-- Create index	  CREATE INDEX idx_name ON table(column);
-- Delete index	  DROP INDEX idx_name ON table;
-- List indexes	  SHOW INDEX FROM table;


-- ====================================================


-- 1. Single Column Index :
CREATE INDEX idx_city ON alumni(City);

-- ----

-- 2. Multi-column (Composite) Index :
CREATE INDEX idx_name_city ON alumni(Name, City);


-- ====================================================

-- How to Delete (Drop) an Index :
DROP INDEX idx_city ON alumni;


-- -----

-- Viewing Existing Indexes : - To list all indexes on a table
SHOW INDEX FROM alumni;

-- ====================================================

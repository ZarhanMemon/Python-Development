
-- Selecting Data from a Table



-- 1. Basic SELECT Statement
SELECT * FROM student;           -- all
SELECT name, age FROM student;   -- specific


-- ---------------------

-- 2. Using the WHERE Clause
SELECT * FROM student WHERE grade = '10th';
SELECT * FROM student WHERE age > 16;


-- ---------------------

-- 3. Comparison Operators in MySQL :

-- Operator	    Description	                      Example
-- =	       Equals	                       WHERE age = 16
-- !=	     Not equal to	                 WHERE grade != '12th'
-- <>	     Not equal to (alternative)	     WHERE grade <> '12th'
-- >	     Greater than	                 WHERE age > 16
-- <	      Less than	                     WHERE age < 17
-- >=	     Greater than or equal to	      WHERE age >= 16
-- <=	      Less than or equal to           WHERE age <= 18
-- BETWEEN	  Within a range (inclusive)	  WHERE age BETWEEN 15 AND 17
-- IN	       Matches any in a list	       WHERE grade IN ('10th', '12th')
-- NOT IN	     Excludes list items	       WHERE grade NOT IN ('9th', '11th')
-- LIKE	        Pattern matching	          WHERE name LIKE 'A%' (names starting with A)
-- NOT LIKE 	Pattern not matching	       WHERE name NOT LIKE '%a' (names not ending in a)


-- ---------------------

-- 4. Handling NULL Values :

-- What is NULL?
--  NULL represents missing or unknown values. It is not equal to 0, empty string, or any other value.

-- Condition	    Correct Syntax
-- Is NULL	       WHERE grade IS NULL
-- Is NOT NULL     WHERE grade IS NOT NULL

SELECT * FROM student WHERE grade IS NULL;
SELECT * FROM student WHERE grade IS NOT NULL;

 
-- ---------------------

-- 5. Combining Conditions ( AND , OR , NOT ) :

SELECT * FROM student WHERE grade = '10th' AND age > 16;
SELECT * FROM student WHERE grade = '10th' OR age > 16;
SELECT * FROM student WHERE NOT grade = '10th' ;


-- ---------------------

-- 6. Sorting Results with ORDER BY :
SELECT * FROM student ORDER BY age ASC;  -- DESC


-- ---------------------

-- 7. Limiting Results with LIMIT :
SELECT * FROM student LIMIT 5;       -- Get only 5 rows
SELECT * FROM student LIMIT 3,5;     -- skip first 3 rows , and return next 5 row to that


-- -------------------


-- 8. Using Wildcards with LIKE :

-- Quick Recap: LIKE Wildcard Matching
-- Pattern	        Meaning
-- 'A%'  	        Starts with A
-- '%sh'	        Ends with sh
-- '%ar%'	        Contains “ar”
-- 'R____'	        5-letter name starting with R
-- '____-__-05'	    Dates with day = 05


 
SELECT * FROM student WHERE admission_date LIKE '____-__-15';   -- Give me all rows where the date ends with -05 — which means the 5th of any month, any year.

SELECT * FROM student WHERE name LIKE 'A%';                     -- This finds any name that starts with 'A', like Aakash, Ananya, Aryan.


-- Pattern to be Matched	Matches
-- '2025-05-%'             	Any day in May 2025
-- '2024-12-__'         	All 2-digit days in December 2024
-- '____-01-01'         	1st January of any year
-- '202_-__-__'          	Any date in the 2020s decade
-- '____-__-3_'	            All dates from day 30 to 39 (not valid, but works syntactically)

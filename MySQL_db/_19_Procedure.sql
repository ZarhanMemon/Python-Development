



-- Stored Procedures in MySQL
-- A Stored Procedure is a saved block of SQL code that you can execute later by calling its name.
-- It allows you to group SQL statements and reuse them—just like a function in programming.


-- ----------

-- Why Use Stored Procedures?
--   \ To avoid repeating the same SQL logic in multiple places
--   \ To improve performance by reducing network traffic
--   \ To encapsulate complex business logic inside the database

-- ------------

--  1.  Creating a Stored Procedure
-- When you create a stored procedure, you need to temporarily change the SQL statement delimiter from ; to something else like // or $$.


-- NOTE :  Why change the DELIMITER?
-- MySQL ends a command at the first ;.
-- Since stored procedures contain multiple SQL statements (each ending in ;), we need to tell MySQL not to end the procedure too early.
-- So we temporarily change the delimiter to something else—then switch it back.



-- Task                  	SQL Command
-- Create Procedure	      CREATE PROCEDURE
-- Change Delimiter     	DELIMITER // (or any unique symbol)
-- Call a Procedure	        CALL procedure_name();
-- With Input Parameter 	IN param_name data_type
-- Drop a Procedure     	DROP PROCEDURE IF EXISTS procedure_name;


-- -> Always give clear names to procedures.
-- -> Use IN, OUT, or INOUT for flexible parameter handling.
-- -> Keep business logic in the database only if it improves clarity or performance.


-- ====================================================

-- Example: Simple Procedure to List All Student

DELIMITER //

CREATE PROCEDURE list_all_student()
BEGIN 
    select * from student_table;
    select * from students;
END //

DELIMITER ;


-- ===========================================

-- 2.  Calling a Stored Procedure :

CALL list_all_student();           -- You use the CALL statement:


-- ===========================================


-- 3. Stored Procedure with Parameters :

-- You can pass values into procedures using the IN keyword.

-- Example: Get details of an studemt by roll_no
DELIMITER //

CREATE PROCEDURE get_student_byRoll( IN num INT)  -- IN -> Here, IN num INT means: “Take an integer input called num when this procedure is called.”
BEGIN 
    select * from student_table
    where roll_no = num;
 END //

DELIMITER ;


CALL get_student_byRoll(3);


-- ===============================================

-- 4.  Dropping a Stored Procedure :
 
DROP PROCEDURE IF EXISTS get_student_byRoll;

-- This ensures it doesn’t throw an error if the procedure doesn’t exist.


-- ===============================================


-- IN Parameters: These are used to pass values into the procedure.
--                The procedure can use these values in its SQL statements, 
--                but any modifications to the parameter within the procedure 
--                are not visible to the caller after the procedure finishes.
--                IN is the default parameter type if none is specified.

-- OUT Parameters: These are used to pass values out of the procedure back to the caller. 
--                 The procedure can modify the value of an OUT parameter,
--                 and the final value is available to the caller after execution.

-- INOUT Parameters: These parameters combine the functionality of IN and OUT. 
--                   A value is passed into the procedure by the caller,
--                   the procedure can modify it, and the modified value is
--                   then returned to the caller. 

DELIMITER //

CREATE PROCEDURE manage_data(
    IN input_id INT,
    OUT output_count INT,
    INOUT inout_status VARCHAR(50)
)
BEGIN
    -- Use IN parameter to select/filter data
    SELECT COUNT(*) INTO output_count FROM students WHERE roll_no = input_id;

    -- Modify INOUT parameter based on internal logic
    IF output_count > 0 THEN
        SET inout_status = 'Found and counted';
    ELSE
        SET inout_status = 'Not found, updating status';
    END IF;
END //

DELIMITER ;



CALL 



-- Stored Procedures in MySQL
-- A Stored Procedure is a saved block of SQL code that you can execute later by calling its name.
-- It allows you to group SQL statements and reuse them—just like a function in programming.


-- ----------

-- Why Use Stored Procedures?
--   \ To avoid repeating the same SQL logic in multiple places
--   \ To improve performance by reducing network traffic
--   \ To encapsulate complex business logic inside the database

-- ------------

--  1.  Creating a Stored Procedure
-- When you create a stored procedure, you need to temporarily change the SQL statement delimiter from ; to something else like // or $$.


-- NOTE :  Why change the DELIMITER?
-- MySQL ends a command at the first ;.
-- Since stored procedures contain multiple SQL statements (each ending in ;), we need to tell MySQL not to end the procedure too early.
-- So we temporarily change the delimiter to something else—then switch it back.



-- Task                  	SQL Command
-- Create Procedure	      CREATE PROCEDURE
-- Change Delimiter     	DELIMITER // (or any unique symbol)
-- Call a Procedure	        CALL procedure_name();
-- With Input Parameter 	IN param_name data_type
-- Drop a Procedure     	DROP PROCEDURE IF EXISTS procedure_name;


-- -> Always give clear names to procedures.
-- -> Use IN, OUT, or INOUT for flexible parameter handling.
-- -> Keep business logic in the database only if it improves clarity or performance.


-- ====================================================

-- Example: Simple Procedure to List All Student

DELIMITER //

CREATE PROCEDURE list_all_student()
BEGIN 
    select * from student_table;
    select * from students;
END //

DELIMITER ;


-- ===========================================

-- 2.  Calling a Stored Procedure :

CALL list_all_student();           -- You use the CALL statement:


-- ===========================================


-- 3. Stored Procedure with Parameters :

-- You can pass values into procedures using the IN keyword.

-- Example: Get details of an studemt by roll_no
DELIMITER //

CREATE PROCEDURE get_student_byRoll( IN num INT)  -- IN -> Here, IN num INT means: “Take an integer input called num when this procedure is called.”
BEGIN 
    select * from student_table
    where roll_no = num;
 END //

DELIMITER ;


CALL get_student_byRoll(3);


-- ===============================================

-- 4.  Dropping a Stored Procedure :
 
DROP PROCEDURE IF EXISTS get_student_byRoll;

-- This ensures it doesn’t throw an error if the procedure doesn’t exist.


-- ===============================================


-- IN Parameters: These are used to pass values into the procedure.
--                The procedure can use these values in its SQL statements, 
--                but any modifications to the parameter within the procedure 
--                are not visible to the caller after the procedure finishes.
--                IN is the default parameter type if none is specified.

-- OUT Parameters: These are used to pass values out of the procedure back to the caller. 
--                 The procedure can modify the value of an OUT parameter,
--                 and the final value is available to the caller after execution.

-- INOUT Parameters: These parameters combine the functionality of IN and OUT. 
--                   A value is passed into the procedure by the caller,
--                   the procedure can modify it, and the modified value is
--                   then returned to the caller. 

DELIMITER //

CREATE PROCEDURE manage_data(
    IN input_id INT,
    OUT output_count INT,
    INOUT inout_status VARCHAR(50)
)
BEGIN
    -- Use IN parameter to select/filter data
    SELECT COUNT(*) INTO output_count FROM student_table WHERE roll_no = input_id;

    -- Modify INOUT parameter based on internal logic
    IF output_count > 0 THEN
        SET inout_status = 'Found and counted';
    ELSE
        SET inout_status = 'Not found, updating status';
    END IF;
END //

DELIMITER ;


-- inputs :
SET @output_count_status = 0;
SET @my_msg = "Nothing";


-- procedure calling returning the the value below
CALL manage_data( 3 , @output_count_status , @my_msg );


-- output:
SELECT @output_count_status, @my_msg;

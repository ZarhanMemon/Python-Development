

-- Transactions in MySQL


-- What is a Transaction?
-- A transaction is a sequence of one or more SQL statements that are executed as a single unit.

-- A transaction has four key properties, known as ACID:
-- Atomicity: All or nothing.
-- Consistency: Valid state before and after.
-- Isolation: Transactions do not interfere.
-- Durability: Changes persist after commit.


-- Statement	        Description
-- AUTOCOMMIT	        Automatically commits every query
-- SET autocommit = 0	Disables autocommit mode
-- COMMIT	            Saves all changes in a transaction
-- ROLLBACK	            Reverts all changes in a transaction


-- -------------------

-- 1.  AUTOCOMMIT :
-- By default, MySQL runs in autocommit mode.
-- This means that every SQL statement is treated as a separate transaction and
-- is committed automatically right after it is executed.
 
SELECT @@autocommit;     -- Check Autocommit Status -> 1/on or  0/off

SET autocommit = 0;    -- Disable Autocommit -> This allows you to group multiple statements into a transaction manually.

SET autocommit = 1;    -- Enable Autocommit


-- -------------------


-- 2.  COMMIT :
-- The COMMIT statement is used to permanently save all the changes made in the current transaction.

START TRANSACTION;

UPDATE  student_table SET age = 100 WHERE roll_no = 1;
UPDATE  student_table SET age = 100 WHERE roll_no = 2;

COMMIT;

-- Once committed, the changes are visible to other sessions 
-- and are stored permanently in the database.


-- --------------

-- 3.  ROLLBACK :
-- The ROLLBACK statement is used to undo changes made in the current transaction. 
-- It is useful if something goes wrong or a condition is not met.

START TRANSACTION;
 
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
 
ROLLBACK;    -- An error or condition check fails here

-- After a rollback, all changes since the start of the transaction are discarded.
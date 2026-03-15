


-- Getting Current Date and Time :

-- Function	             Returns        Example Output
-- CURRENT_DATE	        Date only       2025-05-02
-- CURRENT_TIME	         Time only	    14:23:45
-- NOW()	            Date and time	2025-05-02 14:23:45
-- CURRENT_TIMESTAMP	Date and time	2025-05-02 14:23:45
-- LOCALTIME	        Date and time	2025-05-02 14:23:45



-- --------------------

-- 1. CURRENT_DATE :
SELECT current_date();  -- Returns the current date in YYYY-MM-DD format.

-- ------------------

-- 2. CURRENT_TIME :
SELECT CURRENT_TIME();      -- Returns the current time in HH:MM:SS format.

-- ------------------

-- 3. CURRENT_TIMESTAMP() / NOW() :
SELECT CURRENT_TIMESTAMP;   -- Returns the current date and time.
-- or
SELECT NOW();

-- ------------------

-- 4. LOCALTIME and LOCALTIMESTAMP :
-- These are same as for NOW() and return the current date and time.

SELECT LOCALTIME;
SELECT LOCALTIMESTAMP;

-- These functions return the local date and time of the MySQL server, not the client's time zone.
-- Important Clarification:
-- The "local" in LOCALTIME refers to the time zone configured on the MySQL server, not the user's system.

-- ------------------


-- 5. Using in Table Inserts :

CREATE table logs (
  event varchar(100) ,
  createdAt datetime primary key,
  updatedAt INT
  );
  
INSERT INTO logs ( event , createdAt , updatedAt )
VALUES ( 'data_import' , NOW() , timestampdiff( HOUR , current_timestamp() , localtime() ) );

SELECT * from logs;
DROP table logs;

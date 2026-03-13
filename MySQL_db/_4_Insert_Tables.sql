


-- Insert Data into the Table 

-- ------------------------


-- 1. Insert One Row at a Time:
INSERT INTO student_table (roll_no, name, age,  admission_date) VALUES (1, 'Ayesha Khan', 16,'2007-05-15');
INSERT INTO student_table (roll_no, name, age, admission_date) VALUES (2, 'Ravi Sharma', 17,  '2006-03-22'); 
INSERT INTO student_table (roll_no, name, age, admission_date) VALUES (3, 'Meena Joshi', 15,  NULL);
INSERT INTO student_table (roll_no, name, age, admission_date) VALUES (4, 'Arjun Verma', 18, NULL);

-- ------------------------


-- 2. Insert All Rows at Once:
INSERT INTO student_table ( roll_no, name, age,  admission_date) VALUES 
( 5, 'Ayesha  ', 16,'2027-05-15'),
(  6, '  Khan', 16,'2017-05-15'),
(  7, 'Aye n', 16,'2007-02-15');


select * from student_table;  -- for verfiying data inserted?


import mysql.connector


connection = mysql.connector.connect(
    host="localhost",       # or your DB server IP
    user="root",            # your MySQL username
    password="zarhan123",
    database="test_db"      # your database name
)


cursor = connection.cursor()

# Example: Create a table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT
)
""")

import pandas as pd
import mysql.connector

data = {
    "Name": ["Amit", "Sara", "Rahul", "Neha", "Raj", "Kiran"],
    "Email": [
        "amit@gmail.com",
        "sara@gmail.com",
        "rahul@gmail.com",
        "neha@gmail.com",
        "raj@gmail.com",
        "kiran@gmail.com"
    ],
    "Age": [21, 22, 20, 23, 24, 22],
    "City": ["Pune", "Mumbai", "Delhi", "Bangalore", "Pune", "Mumbai"]
}


df = pd.DataFrame( data )




connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="zarhan",

    database="my_db"
)
print("Connected to MySQL database successfully!")


mysql_cursor = connection.cursor()


mysql_cursor.execute("DROP TABLE IF EXISTS dashboard")

mysql_cursor.execute("""CREATE TABLE IF NOT EXISTS dashboard (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255),
    age INT,
    city VARCHAR(255)
)""")

print("Table created successfully!""")
 

mysql_query = "INSERT INTO dashboard (name, email, age, city) VALUES (%s, %s, %s, %s)"


records = df[["Name", "Email", "Age", "City"]].values.tolist()  
# Convert DataFrame to list of lists for MySQL insertion


mysql_cursor.executemany( mysql_query, records )  
# Insert multiple records into MySQL database using executemany() for efficiency
print("Data inserted into MySQL database successfully!")


mysql_cursor.execute("SELECT * FROM dashboard")
dashboard_rows = mysql_cursor.fetchall()
for row in dashboard_rows:
    print(row)



connection.commit()  # Commit the transaction to save changes to the database
mysql_cursor.close()
connection.close()
import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="NoweHaslo123!",
    database="wsaa"
)

mycursor = connection.cursor()
sql = "SELECT * FROM student where id = %s"
values = (1,)

mycursor.execute(sql, values)
result = mycursor.fetchall()
for x in result:
    print(x)    

mycursor.close()
connection.close()
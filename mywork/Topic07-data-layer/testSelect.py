import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="NoweHaslo123!",
    database="wsaa"
)

cursor = db.cursor()
sql = "SELECT * FROM student where id = %s"
values = (1,)

cursor.execute(sql, values)
result = cursor.fetchall()
for x in result:
    print(x)    

db.close()
cursor.close()

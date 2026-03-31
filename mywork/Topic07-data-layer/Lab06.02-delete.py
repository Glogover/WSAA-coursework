import mysql.connector

connection = mysql.connector.connect(
  host="localhost",
  user="root",
  password="NoweHaslo123!",
  database="wsaa"
)

mycursor = connection.cursor()
sql="delete from student where id = %s"
values = (2,)

mycursor.execute(sql, values)

connection.commit()
print("delete done")

mycursor.close()
connection.close()
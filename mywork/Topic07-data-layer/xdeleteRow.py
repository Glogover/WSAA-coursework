import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="NoweHaslo123!",
  database="wsaa2"
)

cursor = db.cursor()
sql="delete from student where id = %s"
values = (2,)

cursor.execute(sql, values)

db.commit()
print("delete done")

db.close()
cursor.close()
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="NoweHaslo123!"
)

cursor = db.cursor()
cursor.execute("create database wsaa")

db.close()
cursor.close()


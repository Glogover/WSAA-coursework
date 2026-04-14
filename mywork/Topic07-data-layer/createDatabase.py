import mysql.connector # This module allows us to connect to a MySQL database and execute SQL commands from Python.

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="NoweHaslo123!"
)

cursor = db.cursor()
cursor.execute("create database wsaa2")

db.close()
cursor.close()


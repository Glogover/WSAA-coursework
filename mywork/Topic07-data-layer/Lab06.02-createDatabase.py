import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="NoweHaslo123!"
)

mycursor = connection.cursor()
mycursor.execute("CREATE DATABASE wsaa")


mycursor.close()
connection.close()


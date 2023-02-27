import mysql.connector as mysql
myobj=mysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='mili@88877',
)
mycursor=myobj.cursor()
mycursor.execute("create database employee")
mycursor.execute("show databases")
db=mycursor.fetchall()
for i in db:
    print(i)


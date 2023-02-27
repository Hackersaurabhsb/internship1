#simple program to check all the databases


import mysql.connector as mysql
myobj=mysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='mili@88877',
)

mycursor=myobj.cursor()
mycursor.execute("show databases");
db=mycursor.fetchall()
print("------------------------")
print("Databases")
print("------------------------")
for i in db:
    print(i)
myobj.close()
print("connection closed")


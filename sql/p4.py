import mysql.connector as mysql
myobj=mysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='mili@88877',
    database="employee"
)
mycursor=myobj.cursor()
#mycursor.execute("create table factory_four(id int not null auto_increment primary key,name char(50) not Null,phone_number int ,salary int,year_of_joining int)")
mycursor.execute("describe factory_four")
db=mycursor.fetchall()
for i in db:
    print(i)
    
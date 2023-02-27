from tkinter import *
import mysql.connector as mysql
sqlobj=mysql.connect(
    host='localhost',
    username='root',
    password='mili@88877',
    port=3306,
    db='employee'
)
cursor=sqlobj.cursor()
def uploadvalue():
    namesql=namevar.get()
    phonesql=phonevar.get()
    salarysql=salaryvar.get()
    addresssql=addressvar.get()
    query="insert into program1(name,phone_number,salary,address) values(%s,%s,%s,%s)"
    values=[(namesql,phonesql,salarysql,addresssql)]
    cursor.executemany(query,values)
    sqlobj.commit()
   
    print("database updated successfully")
root=Tk()


#variables to store values 
namevar=StringVar()
phonevar=StringVar()
salaryvar=IntVar()
addressvar=StringVar()

#geometry for root
root.geometry("500x400")

#create lables for all the values
name=Label(root,text="Enter Employee Name :",font=(20))
phone=Label(root,text="Enter Phone number :",font=(20))
salary=Label(root,text="Enter The Salary :",font=(20))
address=Label(root,text="Enter the Address :",font=(20))

#create entry widgets to enter the values
nameentry=Entry(root,textvariable=namevar)
phoneentry=Entry(root,textvariable=phonevar)
salaryentry=Entry(root,textvariable=salaryvar)
addressentry=Entry(root,textvariable=addressvar)

#create a heading 
heading=Label(root,text="Employee Management System",fg="blue",font=(35))


#now pack all values one by one 
heading.pack(fill=BOTH)
name.pack()
nameentry.pack(fill=BOTH)
phone.pack()
phoneentry.pack(fill=BOTH)
salary.pack()
salaryentry.pack(fill=BOTH)
address.pack()
addressentry.pack(fill=BOTH)

#create a button to add event listener function
btn=Button(root,text="UPLOAD",font=(20),command=uploadvalue,bg="red",fg="white")
btn.pack()

root.mainloop()
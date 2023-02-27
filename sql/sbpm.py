from tkinter import *
import time
import mysql.connector as mysql
sqlobj=mysql.connect(
    host='localhost',
    username='root',
    password='mili@88877',
    port=3306,
    db='employee'
)
def check():
    frame1.pack_forget()
root=Tk()
root.geometry("1920x1080")
frame1=Frame(root,bg="red",width=1920,height=1080)
welcome_label=Label(frame1,text="Welcome To SBPM School",font=60,fg="white",bg="red")
welcome_label.pack(fill=BOTH)
btn=Button(frame1,text="PAY FEES",command=check,font=30)
btn.pack()
frame1.pack()
frame1.pack_propagate(0)
name_label=Label(root,text="Enter Student's Name ")
class_label=Label(root,text="Enter The Class Of Student")
section_label=Label(root,text="Enter The section of the student")
name_entry=Entry(root)
class_entry=Entry(root)
section_entry=Entry(root)
name_label.pack(fill=BOTH)
name_entry.pack(fill=BOTH)
class_label.pack(fill=BOTH)
class_entry.pack(fill=BOTH)
section_label.pack(fill=BOTH)
section_entry.pack(fill=BOTH)
root.mainloop()
time.sleep(5)
welcome_label.pack_forget()

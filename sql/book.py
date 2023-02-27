from tkinter import *
import mysql.connector as mysql
root=Tk()
root.geometry("500x400")
lbl1=Label(root,text="label 1")
lbl2=Label(root,text="label 2")
lbl3=Label(root,text="label 3")
lbl4=Label(root,text="label 4")

#packing labels

lbl1.grid(row=0,column=0)
lbl2.grid(row=0,column=2)
lbl3.grid(row=1,column=0)
lbl4.grid(row=1,column=2)


entry1=Entry(root)
entry2=Entry(root)
entry3=Entry(root)
entry4=Entry(root)

entry1.grid(row=0,column=1)
entry2.grid(row=0,column=3)
entry3.grid(row=1,column=1)
entry4.grid(row=1,column=3)


root.mainloop()
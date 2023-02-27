from tkinter import *

root=Tk()
root.title("my calculator")
var1=IntVar()
var2=IntVar()
var3=IntVar()
def add():
    import time
    var3=var1.get()+var2.get()
    print(var3)
    lbl3["textvariable"]=var1.get()+var2.get()
    btn1["bg"]="green"
    btn1.update()
    time.sleep(2)
    btn1["bg"]="blue"
root.geometry("400x400")
lbl1=Label(root,text="Enter the first number :",fg="red",font=("Arial",25))
lbl2=Label(root,text="Enter the second number :",fg="green",font=("Arial",25))
ent1=Entry(root,textvariable=var1,font=(40))
ent2=Entry(root,textvariable=var2,font=(40))
lbl1.pack(pady=10)
ent1.pack(fill=X,ipady=10)
lbl2.pack(pady=10)
ent2.pack(fill=X,ipady=10)
btn1=Button(root,text="ADD",bg="blue",fg="white",command=add)
btn1.pack(fill=X,pady=10)
lbl3=Entry(root,textvariable=var3)
lbl3.pack()
root.mainloop()
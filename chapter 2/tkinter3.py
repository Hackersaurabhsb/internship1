from tkinter import *
root=Tk()
lbl1=Label(text="heyyy")
lbl2=Label(text="this is saurabh")
lbl3=Label(text="great hacker")
lbl1.pack()
lbl2.pack()
lbl3.pack()
img=PhotoImage(file="sb.png")
lbl4=Label(image=img)
lbl4.pack()

def button1():
    print("i aam button 1")
bt1=Button(text="submit",command=button1)
bt2=Button(text="cancel")
bt3=Button(text="restart")
bt1.pack()
bt2.pack()
bt3.pack()
root.mainloop()


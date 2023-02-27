#checkboxes in python using tkinter
from tkinter import *
root=Tk()
kinter=IntVar()
def func1():
    print("button is clicked")
def func2():
    if kinter.get()==1:
        print("button selected")
    else:
        print("button unnselected")
btn1=Button(root,text="okkkk",bg="red",fg="white",command=func1)
btn1.pack()
btn2=Checkbutton(root,text="are u a hacker",variable=kinter,command=func2)
btn2.pack()
print(kinter.get())

root.mainloop()


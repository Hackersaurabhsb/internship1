from tkinter import *
root=Tk()
root.geometry("600x600")
btn1=Button(root,text="i am button 1")
btn1.grid(columnspan=5)
btn2=Button(root,text="i am button 2")
btn2.grid(row=1,column=5)
root.mainloop()

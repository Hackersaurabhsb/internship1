from tkinter import *
root=Tk()
def text_display():
    print(e.get())
btn=Button(root,text="submit",command=text_display)
frame1=Frame(root)
lbl=Label(frame1,text="This is frame 1")
btn.pack()
frame1.pack()
lbl.pack()
e=Entry(root)
e.pack()
root.mainloop()
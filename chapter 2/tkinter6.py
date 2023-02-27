from tkinter import *
root=Tk()
def change():
    d=ent.get()
    lbl["text"]=d
btn=Button(root,text="click me to change label",command=change)
lbl=Label(root,text="i am label")
lbl.pack()
ent=Entry(root)
btn.pack()
ent.pack()
root.mainloop()
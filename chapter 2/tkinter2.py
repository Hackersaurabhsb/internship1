from tkinter import *
from PIL import Image,ImageTk
root=Tk()
#width*height
root.geometry("1366x768")
root.minsize(234,342)
#img=PhotoImage(file="sb.png")
img=Image.open("istockphoto-1295274245-170667a.jpg")
photo=ImageTk.PhotoImage(img)
lbl=Label(image=photo)
lbl.pack()
saurabh=Label(text="heyyy i am a great hacker")
saurabh.pack()
root.mainloop()
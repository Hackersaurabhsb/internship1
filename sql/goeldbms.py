from tkinter import *
import mysql.connector as mysql
sqlobj=mysql.connect(
    host='localhost',
    username='root',
    password='mili@88877',
    port=3306,
    db='employee'
)
cursor=sqlobj.cursor();
def uploadvalue():
    pass


root=Tk()
label1=Label(root,text="Enter Product Number")
label2=Label(root,text="Enter The Product  Description")
label3=Label(root,text="Enter The Profit Percent")
label4=Label(root,text="Enter Unit Measure")
label5=Label(root,text="Enter The Quantity On Hand")
label6=Label(root,text="Enter The reorder level")
label7=Label(root,text="Enter The Sell Price")
label8=Label(root,text="Enter the Cost Price")
product_no=Entry(root)
description=Entry(root)
profit_percent=Entry(root)
unit_measure=Entry(root)
qty_on_hand=Entry(root)
reorder=Entry(root)
sell_price=Entry(root)
cost_price=Entry(root)
label1.pack()
product_no.pack()
label2.pack()
description.pack()
label3.pack()
profit_percent.pack()
label4.pack()
unit_measure.pack()
label5.pack()
qty_on_hand.pack()
root.mainloop()

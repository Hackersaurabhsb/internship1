class first:
    i=0
    __j=0
    k=0
    def __init__(self):
        self.i=12
        self.j=45
        self.k=0
    def one(self):
        print("this is function without self")
        print(self.i,self.j,self.k)
class second(first):
    def __init__(self):
        self.i=12
        self.j=23
        self.k=21
    def printmsg(self):
        print(self.i,self.j,self.k)
        print("heyyyy i am from second class")
print("before calling class second the values are :")
d=first()
d.one()
print("After calling class second the values are :")
b=second()
b.printmsg()



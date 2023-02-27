class first:
    i=0
    j=0
    def __init__(self):
        self.i=12
        self.j=23
    def calcsum(self):
        print("sum is ",self.i+self.j)

class second(first):
    k=0
    l=0
    super.__init__()
    def __init__(self):
        self.k=45
        self.l=34
    def calcsub(self):
        print("subtraction is :",self.k-self.l )

class third(second):
    a=0
    b=0
    super.__init__()
    def __init__(self):
        self.a=34
        self.b=89
    def calcmul(self):
        print("multiplication is :",self.a*self.b)


d=third()
c=first()
c.calcsum()
d.calcsum()
d.calcsub()
d.calcmul()

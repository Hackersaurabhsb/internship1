class first:
    a=0
    b=0
    c=0
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def display(self):
        print(self.a,self.b,self.c)
class second(first):
    d=0
    def __init__(self, a, b, c,d):
        self.d=d
        super().__init__(a, b, c)
    def display(self):
        print(self.a,self.b,self.c,self.d)
f=first(45,56,67)
s=second(12, 23, 12, 13)
f.display()
s.display()
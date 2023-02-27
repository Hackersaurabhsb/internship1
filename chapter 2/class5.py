class demo:
    height=0
    weight=0
    def __init__(self):
        self.height=40
        self.weight=50
    def area(self):
        print("area is",self.height*self.weight)
    def __del__(self):
        print("destructor function called")
a=demo()
a.area()
b=demo()
c=demo()

class circle:
    radius=0
    def __init__(self,radius):
        self.radius=radius
    def getradius(self):
        print("Radius of the circle is : ")
        print(self.radius)
    def calc(self):
        print("Area of the circle is :")
        print(3.14*self.radius**2)

class cylinder:
    height=0
    def __init__(self,radius,height):
        self.height=height
        super().__init__(radius)  
    def Calc(self):
        print("Area of the cylinder is :  ")
        print(2*3.14*self.radius*self.height)
c=circle(32)
d=cylinder(12,14)
c.getradius()
c.calc()
d.Calc()    
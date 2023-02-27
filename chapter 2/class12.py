class circle:
    def __init__(self,radius):
        self.radius=radius
    def getradius(self):
        print("radius of the circle :")
        return self.radius
    def calcarea(self):
        return 3.14*self.radius*self.radius
c=circle(2)
print(c.getradius())
print(c.calcarea())
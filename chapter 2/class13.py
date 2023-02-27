class point:
    x=0
    y=0
    def __init__(self):
        self.x=12
        self.y=90
    def display(self):
        print("The coordinates are : ")
        print(f"x={self.x},y={self.y}")
    def translate(self):
        print("moving x in x direction and y in y direction :")
d=point()
d.display()
d.translate()

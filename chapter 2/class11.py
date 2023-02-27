class demo:
    def get(self):
        self.s=input("Enter the string : ")
    def printstring(self):
        print(self.s.upper())
d=demo()
d.get()
d.printstring()

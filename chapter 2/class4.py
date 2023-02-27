class demo:
    def method1(self):
        print("i am method 1")
    def method2(self):
        print("i am method 2")
        self.method1()
d=demo()
d.method2()
print(dir(demo))
print(demo.__dict__)
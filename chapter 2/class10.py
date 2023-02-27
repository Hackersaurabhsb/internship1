class person:
    def __init__(self,id1):
        self.id1=id1
john=person('a123')
print(john.__dict__)
john.__dict__['age']=45
print(len(john.__dict__))
print(john.__dict__)
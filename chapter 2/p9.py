lst=[10,20,30,40]
def modify(lst):
    lst.append(40)
    return lst
lst2=modify(lst)
print(lst2)
print(lst)
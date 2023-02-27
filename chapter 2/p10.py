l=[10,20,30,40,50]
def removefl(l):
    l.remove(l[0])
    l.remove(l[-1])
removefl(l)
print(l)
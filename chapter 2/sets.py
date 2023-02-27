s={'arun','ajeet','banana','basket'}
a=set()
b=set()
print(type(a))
print(type(b))
for i in s:
    if i[0]=='a' or i[0]=='A':
        a.add(i)
    else:
        b.add(i)
print(a)
print(b)
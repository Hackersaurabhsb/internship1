date1=(12,3,2018)
date2=(19,6,2019)
t=[]
s=0
for d in range(len(date1)):
    s=date1[d]-date2[d]
    t.append(abs(s))
print(t)
b=15*12
c=1*365
print(c+b)
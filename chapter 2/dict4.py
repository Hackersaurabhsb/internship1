def orange_cap(lst):
    dhoni=0
    kohli=0
    pujara=0
    d={}
    for keys,values in lst.items():
        for v in values:
            if v not in d:
                d[v]=values[v]
            else:
                d[v]=d[v]+values[v]
    max=0
    print(d)
    for i in d:
        if max<d[i]:
            max=d[i]
            name=i
    print(name,"has highest run",max)
lst={'test1':{'dhoni':12,'kohli':23},'test2':{'dhoni':45,'pujara':34,'kohli':44}}
print(orange_cap(lst))

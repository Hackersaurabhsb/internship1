def count(animals):
    d={}
    count=0
    for key,values in animals.items():
        count=0
        for v in values:
            count+=1
        d[key]=count
    print(max(d,key=d.get))

animals={'L':['lion'],'D':['donkey','deer'],'E':['Elephant']}
count(animals)

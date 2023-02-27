def how_many(animals):
    count=0
    for key,values in animals.items():
        for v in values:
            count+=1
    print("number of  animals are",count)
animals={'L':['lion'],'D':['donkey','deer'],'E':['Elephant']}
how_many(animals)


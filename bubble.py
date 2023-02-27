def bubble(lst):
    for i in range(0,len(lst)):
        for j in range(0,len(lst)-1):
            if lst[j]>lst[j+1]:
                tmp=lst[j]
                lst[j]=lst[j+1]
                lst[j+1]=tmp
    return lst
lst=[2,3,1,4,5,2,6,7,4]
print(bubble(lst))

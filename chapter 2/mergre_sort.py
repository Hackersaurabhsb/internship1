def mergesort(mylist):
    if len(mylist)>1:
        mid=len(mylist)//2
        leftlist=mylist[:mid]
        rightlist=mylist[mid:]
        mergesort(leftlist)
        mergesort(rightlist)
        i=0
        j=0
        k=0
        while i<len(leftlist) and j<len(rightlist):
            if leftlist[i]<rightlist[j]:
                mylist[k]=leftlist[i]
                i=i+1
            else:
                mylist[k]=rightlist[j]
                j=j+1
            k=k+1
        while i<len(leftlist):
            mylist[k]=leftlist[i]
            i=i+1
            k=k+1
        while j<len(rightlist):
            mylist[k]=rightlist[j]
            j=j+1
            k=k+1
mylist=[3,1,2,7,5,6]
print("list before sorting is : ")
print(mylist)
print("List after sorting is : ")
mergesort(mylist)
print(mylist)

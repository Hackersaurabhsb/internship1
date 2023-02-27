l=[5,2,4,1,6,7,9,8]
p=0
for i in range(0,len(l)):
    for j in range(0,len(l)-1):
        if l[j]>l[j+1]:
            p+=1
            temp=l[j]
            l[j]=l[j+1]
            l[j+1]=temp
    if p==0:
        print("loop terminated")
        break
        
    p=0
    print("Running loop")
print(l)

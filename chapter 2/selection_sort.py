l=[3,1,2,5,7,9,8,6]
p=0
for i in range(len(l)):
    minn=l[i]
    pos=i
    for j in range(i+1,len(l)):
        if l[j]<minn:
            pos=j
            minn=l[j]
            p+=1
    l[pos]=l[i]
    l[i]=minn

print(l)
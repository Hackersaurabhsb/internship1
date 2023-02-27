prize=[('mobile',12212),('tv',4545),('tablet',21323)]
print(prize[0][1])
for i in range(len(prize)):
    max=prize[i][1]
    for j in range(0,len(prize)):
        min=prize[j][1]
        if min<max:
            temp=prize[i]
            prize[i]=prize[j]
            prize[j]=temp
        print(prize)
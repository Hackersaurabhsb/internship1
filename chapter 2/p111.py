l=[1,2,3,4,5,6,7,8,9,10]

p=0
l2=[]
def prime(l):
    global p
    for i in l:
        for j in range(i+1,1,-1):
            if i%j==0:
                p=p+1
        if p==2:
            l2.append('true')
        else:
            l2.append('false')
        p=0        
prime(l)
prime(l2)
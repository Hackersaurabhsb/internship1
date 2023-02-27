class demo:
    def prime(self,n):
        for i in range(3,n):
            for j in range(2,i):
                if i%j==0:
                    continue
            print(i)
d=demo()
d.prime(10)
#for i in d.prime(10):
    #print(i)

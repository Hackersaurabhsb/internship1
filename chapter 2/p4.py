p=1;
for i in range(1,8):
        p=1
        if(i<=4):
            for j in range(1,i+1):
                print(p,end="")
                p=p+1
            print()        
        else:
            for k in range(i,8):
                print(p,end="")
                p=p+1
            print()
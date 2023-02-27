#printing diamond pattern
# using multiply property
i=5
for k in range(1,10,2):
    print(" "*i,end="")
    print("*"*k)
    i=i-1
i=1
for k in range(9,0,-2):
    print(" "*i,end="")
    print("*"*k)
    i+=1

 


def unique():
    s=input("Enter a string : ")
    for i in range(len(s)-1,-1,-1):
        yield s[i]
k=unique()
for j in k:
    print(j)
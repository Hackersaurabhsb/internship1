for i in range(0,3):
    s=eval(input())
    if type(s)==int:
        continue
    print(s[0:len(s):2],end=" ")
    print(s[1:len(s):2])


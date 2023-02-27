t=int(input())
s=[]
vowel=['a','e','i','o','u','A','E','I','O','U']
for i in range(t):
    name=input()
    s.append(name)
for i in range(len(s)):
    check=s[i][len(s[i])-1]
    if check=="y" or check=="Y":
        print(f"case #{i+1}: {s[i]} is ruled by nobody")
    elif check in vowel:
         print(f"case #{i+1}: {s[i]} is ruled by Alice")
    else:
        print(f"case #{i+1}: {s[i]} is ruled by Bob")
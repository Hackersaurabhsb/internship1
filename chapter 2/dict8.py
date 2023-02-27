def count(string):
    d={}
    for i in string:
        if i not in d:
            d[i]=1
        else:
            d[i]=d[i]+1
    return d
string="hello"
print(count(string))

def histogram(d):
    p={}
    for c in d:
        if c not in p:
            p[c]=1
        else:
            p[c]=p[c]+1
    return p
print(histogram("apple"))

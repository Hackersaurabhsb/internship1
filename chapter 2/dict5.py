def assign(tupl):
    l=[]
    for i in range(0,len(tupl),2):
        l.append(tupl[i])
    return tuple(l)
tupl=('hello','are','you','python','programmer')
print(assign(tupl))

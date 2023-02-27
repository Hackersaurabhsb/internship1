def tupl():
    t=(
        ('saurabh',89),
        ('akash',88),
        ('chandu',87)
    )
    max=0
    min=0
    tup=()
    for i in range(len(t)-1):
        min=t[i][1]
        if min>=max:
            max=min
            tup=t[i]
    yield tup
        
k=tupl()
for i in k:
    print(i)
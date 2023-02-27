d={'dhoni':{'test':2323,'odi':3434},'sachin':{'test':212,'odi':323}}
for key,values in d.items():
    print("Player Name : ",key)
    print("Achievements :")
    for v in values:
        print(v,':',values[v])
        

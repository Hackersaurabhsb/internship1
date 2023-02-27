def pn(lst):
    d={'positive':0,'negative':0}
    for i in lst:
        if i>0:
            d['positive']=d['positive']+1
        else:
            d['negative']=d['negative']+1
    return d
lst=[10,20,-20,-32,10,23,-34,34]
print(pn(lst))

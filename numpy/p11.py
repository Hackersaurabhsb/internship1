import numpy as np 
from io import StringIO
data=u"1 2 3\n4 5 6"
print(np.genfromtxt(StringIO(data),names="a,b,c",usecols=("a","c")))
print(data)
d=np.arange(18,dtype="float64").reshape(3,6)
print(d)
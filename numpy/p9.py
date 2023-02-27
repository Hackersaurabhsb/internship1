import numpy as np 
from io import StringIO
data=u"1 2 3\n4 5 6"
print(data)
print(np.genfromtxt(StringIO(data),names="a,b,c",usecols=("a","c")))


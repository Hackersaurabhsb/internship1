import numpy as np
from io import StringIO
data=StringIO("1 2 3\n4 5 6")
names="a,b,c"
ndtype=[('a',int),('b',float),('c',int)]
print(np.genfromtxt(data,names=names,dtype=ndtype))
import numpy as np 
from io import StringIO
data=StringIO("1 2 3\n 4 5 6")
print(np.genfromtxt(data,dtype=[(_,float) for _ in "abc"]))
print(data)


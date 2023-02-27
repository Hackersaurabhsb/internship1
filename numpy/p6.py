import numpy as np 
from io import StringIO
data=u"1, abc , 2\n 3, xxx , 4"
print(np.genfromtxt(StringIO(data),delimiter=",", dtype="|U5",autostrip=True))

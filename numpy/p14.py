import numpy as np 
from io import StringIO
c=lambda x:float(x.strip() or 999)
data=u"1, ,3\n4,5,6"
print(np.genfromtxt(StringIO(data),delimiter=",",converters={1:c}))
